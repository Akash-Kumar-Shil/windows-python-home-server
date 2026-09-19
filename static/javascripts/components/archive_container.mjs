import { setStyles, useState } from "../modules/Arow.mjs";
import { getData } from "../modules/Utilities.mjs";

function ARCHIVE_BOX(url = "", name = "") {
    return `
    <a href="${url}" class="archive_box369">
        <span class="icon"><i class="ri-folder-zip-fill"></i></span>
        <span>${name.split("/")[1] || ""}</span>
    </a>
    `
}

setStyles(".archive_box369", `
    display: flex;
    align-items: center;
    gap: 0.5rem;
    width: 20rem;
    overflow: hidden;
    outline: 1px solid currentColor;
    border-radius: 0.3rem;
    padding: 0.5rem;
    background-color: hsl(from currentColor h s l / 0.2);
    color: gray;
    cursor: pointer;
    white-space: nowrap;
    text-overflow: ellipsis;
    text-decoration: none;
        transition: all linear 0.5s;
    
    &:hover {
        color: #8fd829;
    }

    .icon {
        font-size: 2.5rem;
    }

    span {
        font-size: 1.2rem;
    }
    `)

const [archive, setArchive] = useState(await getData("Archives"));

export function ARCHIVE_CONTAINER() {
    const currentData = archive();
    const fileList = currentData?.files || [];

    return `
    <div id="archive_container369">
            ${fileList.map((file) => ARCHIVE_BOX(`file/${file}`, file)).join("")}
    </div>`
}

setStyles("#archive_container369", `
        display: flex;
        justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    `)