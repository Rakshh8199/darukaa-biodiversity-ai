const API_URL = "http://127.0.0.1:8000";

async function search() {

    const queryInput = document.getElementById("query");
    const resultsDiv = document.getElementById("results");
    const statusDiv = document.getElementById("status");

    const query = queryInput.value.trim();

    if (!query) {
        statusDiv.innerHTML = `
            <p class="warning">
                Please enter a question.
            </p>
        `;
        resultsDiv.innerHTML = "";
        return;
    }

    statusDiv.innerHTML = `
        <p class="loading">
            Searching biodiversity knowledge base...
        </p>
    `;

    resultsDiv.innerHTML = "";

    try {

        const response = await fetch(
            API_URL + "/search?q=" + encodeURIComponent(query)
        );

        if (!response.ok) {
            throw new Error("Backend request failed");
        }

        const data = await response.json();

        statusDiv.innerHTML = "";

        if (!data.results || data.results.length === 0) {

            resultsDiv.innerHTML = `
                <div class="no-results">
                    <h2>No matching information found</h2>

                    <p>
                        No knowledge-base entry was found for:
                        <strong>${escapeHTML(query)}</strong>
                    </p>

                    <p>
                        Try a broader environmental or biodiversity term.
                    </p>
                </div>
            `;

            return;
        }

        resultsDiv.innerHTML = `
            <h2>Knowledge Base Results</h2>

            ${data.results.map(item => createResultCard(item)).join("")}
        `;

    } catch (error) {

        console.error(error);

        statusDiv.innerHTML = `
            <p class="error">
                Could not connect to the AI backend.
            </p>
        `;

        resultsDiv.innerHTML = `
            <div class="error-card">
                <h2>Backend Connection Error</h2>

                <p>
                    Make sure your FastAPI server is running.
                </p>

                <code>uvicorn app.main:app --reload</code>
            </div>
        `;
    }
}


function createResultCard(item) {

    const title = escapeHTML(
        item.title || "Environmental Knowledge"
    );

    const content = escapeHTML(
        item.content || "No description available."
    );

    const topic = item.topic
        ? escapeHTML(item.topic)
        : "";

    const source = item.source
        ? escapeHTML(item.source)
        : "";

    let metricsHTML = "";

    if (Array.isArray(item.metrics) && item.metrics.length > 0) {

        metricsHTML = `
            <div class="metrics">
                <strong>Environmental Metrics</strong>

                <div class="metric-list">
                    ${item.metrics.map(metric => `
                        <span>${escapeHTML(String(metric))}</span>
                    `).join("")}
                </div>
            </div>
        `;
    }

    return `
        <div class="result-card">

            <h3>${title}</h3>

            ${topic
                ? `<p class="topic">
                    <strong>Topic:</strong> ${topic}
                   </p>`
                : ""
            }

            <p class="content">
                ${content}
            </p>

            ${metricsHTML}

            ${source
                ? `<p class="source">
                    <strong>Scientific Source:</strong> ${source}
                   </p>`
                : ""
            }

        </div>
    `;
}


function useExample(example) {

    document.getElementById("query").value = example;

    search();
}


function escapeHTML(value) {

    return value
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


document.getElementById("query").addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {
            search();
        }

    }
);