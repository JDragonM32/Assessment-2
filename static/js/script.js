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