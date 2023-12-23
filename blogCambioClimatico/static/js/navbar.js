// Obtiene el nombre del archivo HTML actual
var pathname = window.location.pathname;

// Cambia el comportamiento del navbar según la página actual
if (pathname === "/") { // Si la página actual es el index
    document.addEventListener('scroll', function() {
        var navbar = document.getElementById('navbar');
        var section = document.getElementById('categorias'); // Sección que marca el límite para cambiar el navbar, en este caso la primer seccion
        navbar.classList.remove('scroll-bg');
        var scrollPosition = window.scrollY;

        if (scrollPosition >= section.offsetTop) {
            navbar.classList.add('scroll-bg');
        } else {
            navbar.classList.remove('scroll-bg');
        }
    });
} else {
    document.getElementById("navbar").classList.add("scroll-bg");

    }


    



