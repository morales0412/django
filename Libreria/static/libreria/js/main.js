document.addEventListener('DOMContentLoaded', function () {
    console.log('Archivo JS cargado correctamente');

    const enlaces = document.querySelectorAll('a');

    enlaces.forEach(link => {
        link.addEventListener('mouseover', () => {
            link.style.color = '#ff6600';
        });

        link.addEventListener('mouseout', () => {
            link.style.color = '#0066cc';
        });
    });
});
