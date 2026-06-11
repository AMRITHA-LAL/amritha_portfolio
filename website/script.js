// PROJECTS

fetch("projects.json")

.then(response => response.json())

.then(projects => {

    const container =
    document.getElementById(
    "projects-container"
    );

    document.getElementById(
    "count"
    ).innerHTML =
    `Total Projects: ${projects.length}`;

    projects.forEach(project => {

        const card =
        document.createElement("div");

        card.className =
        "project-card";

        card.innerHTML = `
        <h3>${project.name}</h3>
        <p>${project.description || "No Description"}</p>
        <a href="${project.url}" target="_blank">
        Open Repository
        </a>
        `;

        container.appendChild(card);

    });

});


// NEWS

fetch("news.json")

.then(response => response.json())

.then(news => {

    const container =
    document.getElementById(
    "news-container"
    );

    const list =
    document.createElement("ul");

    news.forEach(item => {

        const li =
        document.createElement("li");

        li.textContent = item;

        list.appendChild(li);

    });

    container.appendChild(list);

});