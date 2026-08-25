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
