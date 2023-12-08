document.addEventListener('DOMContentLoaded', function () {
  // Obtener todos los dropdowns en la página
  var dropdowns = document.querySelectorAll('.filtro-dropdown');

  // Iterar sobre cada dropdown
  dropdowns.forEach(function(dropdown) {
    // Obtener elementos específicos de cada dropdown
    var dropdownButton = dropdown.querySelector('.dropdown-toggle');
    var dropdownItems = dropdown.querySelectorAll('.dropdown-item');

    // Asignar evento de clic a cada elemento del dropdown
    dropdownItems.forEach(function(item) {
      item.addEventListener('click', function() {
        // Obtener el valor de la opción clickeada
        var selectedValue = item.getAttribute('data-value');

        // Establecer la clase 'active' en la opción clickeada
        dropdownItems.forEach(function(item) {
          item.classList.remove('active');
        });
        item.classList.add('active');

        // Actualizar el texto del botón con la opción clickeada
        dropdownButton.textContent = item.textContent;
      });
    });

    // Establecer la opción por defecto al cargar la página
    var defaultOptionValue = "default"; // Cambia esto al valor que desees seleccionar por defecto
    var defaultOption = dropdown.querySelector('.dropdown-menu [data-value="' + defaultOptionValue + '"]');
    defaultOption.classList.add('active');
    dropdownButton.textContent = defaultOption.textContent;
  });
});
