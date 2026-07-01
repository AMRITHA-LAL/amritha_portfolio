const cards =
document.querySelectorAll(".gallery-card");

const count =
document.getElementById("project-count");

function updateCount(){

    const visible =
    document.querySelectorAll(
    ".gallery-card:not(.hide)"
    ).length;

    count.innerText =
    `Showing ${visible} Projects`;
}

function filterProjects(category){

    cards.forEach(card => {

        if(
            category === "all" ||
            card.classList.contains(category)
        ){
            card.classList.remove("hide");
        }
        else{
            card.classList.add("hide");
        }

    });

    updateCount();
}

updateCount();
fetch("projects.json")

.then(response => response.json())

.then(projects => {

    document.getElementById(
        "repo-count"
    ).innerText =

    `Total Repositories: ${projects.length}`;

    const container =
    document.getElementById(
        "repo-container"
    );

    container.innerHTML = "";

    projects.forEach(project => {

        const card =
        document.createElement(
            "div"
        );

        card.className =
        "project-card";

        card.innerHTML = `

            <h3>${project.name}</h3>

            <p>
            ${project.description || "No Description"}
            </p>

            <a href="${project.url}"
               target="_blank">

               View Repository

            </a>
        `;

        container.appendChild(card);

    });

});
let currentSlide = 0;


const slides = document.querySelectorAll(".slide");


const titles = [
    "Login Screen",
    "Home Dashboard",
    "Tasks Management",
    "Calendar",
    "AI Assistant Interface",
    "User Profile"
];


function showSlide(index){

    slides.forEach(slide=>{
        slide.classList.remove("active");
    });


    slides[index].classList.add("active");


    document.getElementById("slide-title").innerHTML =
    titles[index];

}



function nextSlide(){

    currentSlide++;

    if(currentSlide >= slides.length){
        currentSlide = 0;
    }

    showSlide(currentSlide);

}



function previousSlide(){

    currentSlide--;

    if(currentSlide < 0){
        currentSlide = slides.length-1;
    }

    showSlide(currentSlide);

}



// Automatic slideshow

setInterval(nextSlide,4000);
