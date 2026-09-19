import { Arow } from "./modules/Arow.mjs"

// components
import { SERVER_MENU } from "./components/Nav.mjs";
import { ARCHIVE_CONTAINER } from "./components/archive_container.mjs";

Arow.templateFun = () => `
${SERVER_MENU()}
${ARCHIVE_CONTAINER()}
`;

Arow.render();
