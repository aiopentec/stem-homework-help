let searchIndex = [];

async function loadSearchIndex() {
    const response = await fetch("/data/search.json");
    searchIndex = await response.json();
}

function searchQuestions(query) {

    query = query
        .toLowerCase()
        .trim();

    if (!query) {
        return [];
    }

    const terms = query.split(/\s+/);

    return searchIndex
        .map(item => {

            let score = 0;

            const title =
                item.title.toLowerCase();

            const text = [
                item.title,
                item.description || "",
                item.topic || "",
                ...(item.concepts || [])
            ]
            .join(" ")
            .toLowerCase();

            for (const term of terms) {

                if (title.includes(term)) {
                    score += 10;
                }

                if (text.includes(term)) {
                    score += 3;
                }
            }

            return {
                item,
                score
            };
        })
        .filter(result => result.score > 0)
        .sort(
            (a, b) =>
                b.score - a.score
        )
        .slice(0, 20);
}

function escapeHtml(text) {
    const div = document.createElement("div");
    div.textContent = text;
    return div.innerHTML;
}

function renderResults(results) {

    const container = document.getElementById("search-results");

    if (!container) {
        return;
    }

    if (results.length === 0) {
        container.innerHTML = "<p>No matching problems found.</p>";
        return;
    }

    const items = results
        .map(({ item }) => {
            return `<li><a href="${item.url}">${escapeHtml(item.title)}</a></li>`;
        })
        .join("");

    container.innerHTML = `<ul class="search-result-list">${items}</ul>`;
}

document.addEventListener("DOMContentLoaded", async () => {

    const input = document.getElementById("search-input");
    const container = document.getElementById("search-results");

    if (!input || !container) {
        return;
    }

    await loadSearchIndex();

    // Homepage search form submits here as ?q=... — pick it up if present.
    const params = new URLSearchParams(window.location.search);
    const initialQuery = params.get("q");

    if (initialQuery) {
        input.value = initialQuery;
        renderResults(searchQuestions(initialQuery));
    }

    input.addEventListener("input", () => {
        renderResults(searchQuestions(input.value));
    });
});
