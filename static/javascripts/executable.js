import { Arow } from "./modules/Arow.mjs"

// components
import { SERVER_MENU } from "./components/Nav.mjs";

Arow.templateFun = () => `
${SERVER_MENU()}
`;

Arow.render();
