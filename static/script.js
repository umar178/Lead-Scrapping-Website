function toggleMenu() {
    const menu = document.getElementById('menu');
    if (menu.style.display === 'block') {
        menu.style.display = 'none';
    } else {
        menu.style.display = 'block';
    }
}

function showProject(){
    var m = document.getElementById("Members");
    var p = document.getElementById("project");
    var s = document.getElementById("scope-of-work");
    var f = document.getElementById("functionality");

    p.style.display = "block";
    m.style.display = "none";
    s.style.display = "none";
    f.style.display = "none";
}

function showMembers(){
    var m = document.getElementById("Members");
    var p = document.getElementById("project");
    var s = document.getElementById("scope-of-work");
    var f = document.getElementById("functionality");

    m.style.display = "block";
    p.style.display = "none";
    s.style.display = "none";
    f.style.display = "none";
}

function showScope(){
    var m = document.getElementById("Members");
    var p = document.getElementById("project");
    var s = document.getElementById("scope-of-work");
    var f = document.getElementById("functionality");

    m.style.display = "none";
    p.style.display = "none";
    s.style.display = "block";
    f.style.display = "none";
}

function showFunctionality(){
    var m = document.getElementById("Members");
    var p = document.getElementById("project");
    var s = document.getElementById("scope-of-work");
    var f = document.getElementById("functionality");

    m.style.display = "none";
    p.style.display = "none";
    s.style.display = "none";
    f.style.display = "block";
}
