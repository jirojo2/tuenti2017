// s => matrix
// c => words

function findNextLetter(word, offset, x, y, dx, dy) {
    let letter = word[offset];
    if (dx || dy) {
        let i = x+dx
        let j = y+dy
        if (i < 0 || j < 0 || j >= s.length || i >= s[j].length) {
            return null;
        }
        else if (s[j][i] === letter) {
            //console.log(`  found letter ${s[j][i]} at (${i}, ${j})`)
            if (offset == word.length-1) {
                return [i, j]
            }
            return findNextLetter(word, offset+1, i, j, dx, dy);
        }
        else {
            //console.log(`  could not find letter ${letter}`)
            return null;
        }
    }
    for (let j = y-1; j < y+2; j++) {
        for (let i = x-1; i < x+2; i++) {
            if (i < 0 || j < 0 || j >= s.length || i >= s[j].length) {
                continue;
            }
            if (i == x && j == y) {
                continue;
            }
            if (s[j][i] === letter) {
                //console.log(`  found letter ${s[j][i]} at (${i}, ${j})`)
                if (offset == word.length-1) {
                    return [i, j]
                }
                else {
                    let pos = findNextLetter(word, offset+1, i, j, i-x, j-y)
                    if (pos) {
                        return pos
                    }
                }
            }
        }
    }
    //console.log(`  could not find letter ${letter}`)
    return null;
}

function findWord(word) {
    console.log(`word to find: ${word}`)
    for (let y = 0; y < s.length; y++){
        for (let x = 0; x < s[y].length; x++) {
            if (s[y][x] === word[0]) {
                //console.log(`  found letter ${s[y][x]} at (${x}, ${y})`)
                let next = findNextLetter(word, 1, x, y)
                if (!next) continue;
                return [x, y].concat(next);
            }
        }
    }
    return null;
}

const m = t => {
    let n, e, o, s = 0;
    const c = t + "-saltbae";
    if (!c.length) return s;
    for (n = 0, o = c.length; n < o; n++) e = c.charCodeAt(n), s = (s << 5) - s + e, s |= 0;
    return Math.abs(s) }

console.log(s)
console.log(c)
for (word of c) {
    let = pos = findWord(word);
    console.log(pos);
    let e = pos.join('-');
    w.send(btoa(`${e}-${m(e)}`));
}
