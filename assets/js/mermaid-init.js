(function () {
  function getMermaidTheme() {
    var skin = document.documentElement.getAttribute("data-theme");
    return skin === "dark" ? "dark" : "default";
  }

  function convertCodeBlocks() {
    var codeBlocks = document.querySelectorAll("pre > code.language-mermaid, pre > code.mermaid");

    codeBlocks.forEach(function (codeBlock) {
      var container = document.createElement("div");
      container.className = "mermaid";
      container.textContent = codeBlock.textContent;
      codeBlock.parentNode.replaceWith(container);
    });
  }

  function renderMermaid() {
    if (!window.mermaid) {
      return;
    }

    convertCodeBlocks();

    window.mermaid.initialize({
      startOnLoad: false,
      theme: getMermaidTheme(),
      securityLevel: "strict"
    });

    window.mermaid.run({
      querySelector: ".mermaid"
    }).catch(function (error) {
      console.warn("Mermaid diagram rendering failed:", error);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", renderMermaid);
  } else {
    renderMermaid();
  }
})();
