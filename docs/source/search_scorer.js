// Search ranking for edisonrul.ing, used through Sphinx's `html_search_scorer`
// setting (see conf.py).
//
// Sphinx's own search still decides which pages match. This only changes the
// order, so that a card whose name matches what you typed comes first:
//
//   1. the card's name is exactly what you typed       "mirror force"
//   2. the card's name starts with what you typed      "cyber drag"
//   3. every word you typed starts a word in the name  "dark mag", "blue eyes"
//   4. everything else, in Sphinx's usual order
//
// Names are compared ignoring case and punctuation, so "blue eyes white
// dragon" matches "Blue-Eyes White Dragon".

var Scorer = {
  // Sphinx's default weights, unchanged (sphinx/themes/basic/static/searchtools.js).
  objNameMatch: 11,
  objPartialMatch: 6,
  objPrio: { 0: 15, 1: 5, 2: -5 },
  objPrioDefault: 0,
  title: 15,
  partialTitle: 7,
  term: 5,
  partialTerm: 2,

  // Points added on top of Sphinx's score for each kind of name match.
  // They are far above anything Sphinx gives, so they decide the order.
  exactName: 3000,
  nameStartsWithQuery: 2000,
  everyWordStartsANameWord: 1000,

  // Called by Sphinx for every result: [docname, title, anchor, descr, score, ...]
  score: (result) => {
    const [, title, anchor, , score] = result;
    // Only boost whole card pages, not sections within a page.
    if (anchor) return score;

    const query = words(currentQuery());
    const name = words(title);
    if (query.length === 0) return score;

    if (name.join(" ") === query.join(" ")) return score + Scorer.exactName;
    if (name.join(" ").startsWith(query.join(" "))) return score + Scorer.nameStartsWithQuery;
    if (query.every((q) => name.some((n) => n.startsWith(q))))
      return score + Scorer.everyWordStartsANameWord;
    return score;
  },
};

// The text being searched for: the search box being typed in, or the
// ?q= part of the address on the search results page.
function currentQuery() {
  const box = document.activeElement;
  if (box && box.name === "q") return box.value;
  return new URLSearchParams(window.location.search).get("q") || "";
}

// "Blue-Eyes White Dragon" -> ["blue", "eyes", "white", "dragon"]
function words(text) {
  return text.toLowerCase().split(/[^\p{Letter}\p{Number}]+/u).filter(Boolean);
}
