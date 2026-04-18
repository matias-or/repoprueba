import { dataMascota } from "../data/dataMascota.js";

const getAll = () => {
    const tBody = document.getElementById('tbodyMascota');
    tBody.innerHTML = '';
    dataMascota.forEach(x => {
        const fila = `
        <tr>
            <td>${x.id}</td>
            <td>${x.name}</td>
            <td>${x.description}</td>
            <td>${x.price}</td>
        </tr>
        `;
        tBody.innerHTML += fila;
    });
}

getAll();