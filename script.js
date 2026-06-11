// =====================
// GITHUB PROJECTS
// =====================

fetch("projects.json")

.then(response => response.json())

.then(projects => {

document.getElementById(
"count"
).innerHTML =

`Total Projects: ${projects.length}`;

const container =
document.getElementById(
"projects-container"
);

container.innerHTML = "";

projects.forEach(project => {

const card =
document.createElement(
"div"
);

card.className =
"project-card";

card.innerHTML =

`
<h3>${project.name}</h3>

<p>
${project.description || "No Description"}
</p>

<a href="${project.url}" target="_blank">
Open Repository
</a>
`;

container.appendChild(
card
);

});

})

.catch(error => {

console.log(error);

});

// =====================
// NEWS HEADLINES
// =====================

fetch("news.json")

.then(response => response.json())

.then(news => {

const container =
document.getElementById(
"news-container"
);

container.innerHTML = "";

const newsBox =
document.createElement(
"div"
);

newsBox.className =
"project-card";

let newsHTML = "<ul>";

news.forEach(item => {

newsHTML +=

`<li>${item}</li>`;

});

newsHTML += "</ul>";

newsBox.innerHTML =
newsHTML;

container.appendChild(
newsBox
);

})

.catch(error => {

console.log(error);

});