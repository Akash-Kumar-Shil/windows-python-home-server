import { Arow, useState } from "./modules/Arow.mjs"

// components
import { SERVER_MENU } from "./components/Nav.mjs";
import { IMAGE_CONTAINER } from "./components/Image_container.mjs";


Arow.templateFun = () => {
    return `
        ${SERVER_MENU()}
        ${IMAGE_CONTAINER()}
    `;
};

Arow.render();
