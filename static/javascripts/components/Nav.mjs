import { setStyles, Arow } from "../modules/Arow.mjs";

// 1. Unified structure: [iconHtml, color (optional)]
const menuLinks = {
  "": [`<i class="fa-solid fa-house"></i>`, "#2373F4"],
  image: [`<i class="fa-solid fa-image"></i>`, "#F54927"],
  video: [`<i class="fa-solid fa-film"></i>`, "#F5B027"],
  music: [`<i class="fa-solid fa-music"></i>`, "#615FFF"],
  document: [`<i class="fa-solid fa-file"></i>`, "#31D492"],
  executable: [`<i class="fa-solid fa-chess-knight"></i>`, "#FF637E"],
  archive: [`<i class="fa-solid fa-file-zipper"></i>`, "#9AE630"]
};

function link(pathKey, iconHtml) {
  const path = `/${pathKey}`;
  // Set initial active class matching current URL path
  const isActive = window.location.pathname === path ? "active" : "";
  const title = pathKey === "" ? "HOME" : pathKey.toUpperCase();

  return `
    <a href="${path}" class="nav-btn ${isActive}" title="${title}">
      ${iconHtml}
    </a>
  `;
}

export function SERVER_MENU() {
  // 2. Destructure icon correctly
  const linksMarkup = Object.entries(menuLinks)
    .map(([key, [icon]]) => link(key, icon))
    .join("");

  return `
    <div id="server_menu369">
      <menu class="box">
        ${linksMarkup}
      </menu>
    </div>
  `;
}

// 3. Dynamic nth-child CSS generator
const iconColor = Object.entries(menuLinks)
  .map(([key, [icon, color]], index) => {
    // Only generate CSS rules if a color is defined
    if (!color) return "";
    return `
    &:nth-child(${index + 1}) { color: ${color}; }
    &:hover:nth-child(${index + 1}),
    &.active:nth-child(${index + 1}) { 
      border: 2px solid ${color};
      box-shadow: 0 0 8px 0 ${color}; 
    }
    `;
  })
  .join("\n");

setStyles(
  "#server_menu369",
  `
  margin: 1.3rem;
  @media (max-width: 768px) {
    margin: 1rem;
  }

  menu {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
    border-radius: 0.5rem;
    padding: 1rem;
    font-size: 1.5rem;

    .active {
    outline: 1px solid currentColor;
}

    a {
      flex-grow: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      height: calc(1em + 2rem);
      aspect-ratio: 1;
      padding: 0.5rem;
      border-radius: inherit;
      background-color: hsl(from currentColor h s l / 0.2);
      color: gainsboro;
      text-align: center;
      text-decoration: none;
      transition: all 0.2s linear;

      ${iconColor}

      &:hover, &.active {
        transform: scale(1.05);
      }
    }
  }
  `
);

Arow.event("#server_menu369", "click", (e) => {
  // Find the closest anchor tag in case user clicks the child <i> icon directly
  const clickedBtn = e.target.closest("a.nav-btn");
  if (!clickedBtn) return;

  // Remove active class from all menu buttons
  document.querySelectorAll("#server_menu369 a.nav-btn").forEach((btn) => {
    btn.classList.remove("active");
  });

  // Add active class to clicked element
  clickedBtn.classList.add("active");
});