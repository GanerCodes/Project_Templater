function createElement(tagName, attrs = {}, ...children) {
  const elem = Object.assign(document.createElement(tagName), attrs);
  for(const child of children) {
    elem.append(...(Array.isArray(child) ? child : [child]));
  }
  return elem;
}
  
const name = 'Geoff'
const app = (—xd.jsx_—)

window.document.getElementById('app').replaceWith(app)