document.addEventListener("DOMContentLoaded", () => {

    const PAGE_SIZE = 20;

    const button = document.querySelector(".load-more-btn");
    const list = document.querySelector(".post-list");

    if (!button || !list) {
        return;
    }

    button.addEventListener("click", () => {

        const hidden = list.querySelectorAll("li.hidden-post");

        Array.prototype.slice.call(hidden, 0, PAGE_SIZE)
            .forEach(item => item.classList.remove("hidden-post"));

        if (list.querySelectorAll("li.hidden-post").length === 0) {
            button.remove();
        }
    });
});
