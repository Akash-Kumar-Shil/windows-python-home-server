import { setStyles, Arow, useState } from "../modules/Arow.mjs";
import { getData } from "../modules/Utilities.mjs";

function IMAGE_BOX(url="", name="") {
    return `
    <a href="${url}" class="image_box369">
    <img src="${url}">
    <span>${name.split("/")[1] || ""}</span>
    </a>
    `
}

setStyles(".image_box369", `
    display: flex;
        flex-direction: column;
        gap: 0.3rem;
        width: 100%; /* Fills the grid column properly */
        box-sizing: border-box;
        break-inside: avoid; /* Prevents card breaking across columns */
        margin-bottom: 1rem;
        overflow: hidden;
        border: none;
        border-radius: 0.5rem;
        padding: 0.5rem;
        background-color: hsl(from currentColor h s l / 0.2);
        color: gray;
        text-decoration: none;
        transition: all linear 0.5s;

        &:hover {
        color: #F54927;
        }

        img {
            width: 100%;
            height: auto;
            display: block;
            border-radius: 0.375rem; /* Slight radius inner fit */
            object-fit: cover;
        }

        span {
            display: block; /* Ensures width truncation works in flexbox */
            width: 100%;
            min-width: 0;
            overflow: hidden;
            white-space: nowrap;
            text-overflow: ellipsis;
        }
    `)

const [images, setImages] = useState(await getData("Images"));

export function IMAGE_CONTAINER() {
    const currentData = images();
    const fileList = currentData?.files || [];

    return `
    <div id="image_container369">
            ${fileList.map((file) => IMAGE_BOX(`file/${file}`, file)).join("")}
    </div>
    `
}

setStyles("#image_container369", `
    columns: 4 300px;
    column-gap: 1rem;
    width: 100%;

    @media (max-width: 768px) {
        columns: 2 150px;
    }
`)