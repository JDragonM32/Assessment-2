   function toggleimage(imageid, buttonid) {
        const img = document.getElementById(imageid);
        const btn = document.getElementById(buttonid);

        document.querySelectorAll('img').forEach(img => {
            img.style.display = 'none';
        });

        document.querySelectorAll('button').forEach(btn => {
            btn.classList.remove('clicked');
        });

        btn.classList.add('clicked');
        img.style.display = 'block';
    }

    document.addEventListener('DOMContentLoaded', () => {
        const currenturl = window.location.href;
        const navLinks = document.querySelectorAll(".nav-link");

        navLinks.forEach(link => {
            if (link.href === currenturl) {
                link.classList.add("active");
            }
        });
    });function toggleimage(imageid, buttonid) {
    const img = document.getElementById(imageid);
    const btn = document.getElementById(buttonid);

    if(btn.classList.contains('clicked')){
        btn.classList.remove('clicked');
        img.style.display = 'none';
    }
    else{
        document.querySelectorAll('img').forEach(img => {
            img.style.display = 'none';
        });

        document.querySelectorAll('button').forEach(btn => {
            btn.classList.remove('clicked');
        });

        btn.classList.add('clicked');
        img.style.display = 'block';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const currenturl = window.location.href;
    const navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(link => {
        if (link.href === currenturl) {
            link.classList.add("active");
        }
    });
});