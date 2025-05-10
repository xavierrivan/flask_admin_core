document.getElementById('pais').addEventListener('change', function(){
  fetch(`/admin/provincias/${this.value}`)
    .then(res => res.json())
    .then(data => {
      let prov = document.getElementById('provincia');
      prov.innerHTML = '';
      data.forEach(o => {
        let opt = document.createElement('option');
        opt.value = o.id; opt.text = o.nombre;
        prov.appendChild(opt);
      });
    });
});
// Al cargar la página, dispara el evento para llenar provincias iniciales
document.getElementById('pais').dispatchEvent(new Event('change'));
