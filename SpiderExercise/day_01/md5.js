var hexcase = 0
  , b64pad = "";
function hex_md5(d) {
    return rstr2hex(rstr_md5(str2rstr_utf8(d)))
}
function b64_md5(d) {
    return rstr2b64(rstr_md5(str2rstr_utf8(d)))
}
function any_md5(d, a) {
    return rstr2any(rstr_md5(str2rstr_utf8(d)), a)
}
function hex_hmac_md5(d, a) {
    return rstr2hex(rstr_hmac_md5(str2rstr_utf8(d), str2rstr_utf8(a)))
}
function b64_hmac_md5(d, a) {
    return rstr2b64(rstr_hmac_md5(str2rstr_utf8(d), str2rstr_utf8(a)))
}
function any_hmac_md5(d, a, b) {
    return rstr2any(rstr_hmac_md5(str2rstr_utf8(d), str2rstr_utf8(a)), b)
}
function md5_vm_test() {
    return hex_md5("abc").toLowerCase() == "900150983cd24fb0d6963f7d28e17f72"
}
function rstr_md5(d) {
    return binl2rstr(binl_md5(rstr2binl(d), d.length * 8))
}
function rstr_hmac_md5(d, a) {
    var b = rstr2binl(d);
    if (b.length > 16)
        b = binl_md5(b, d.length * 8);
    var c = Array(16);
    d = Array(16);
    for (var e = 0; e < 16; e++) {
        c[e] = b[e] ^ 909522486;
        d[e] = b[e] ^ 1549556828
    }
    a = binl_md5(c.concat(rstr2binl(a)), 512 + a.length * 8);
    return binl2rstr(binl_md5(d.concat(a), 640))
}
function rstr2hex(d) {
    for (var a = hexcase ? "0123456789ABCDEF" : "0123456789abcdef", b = "", c, e = 0; e < d.length; e++) {
        c = d.charCodeAt(e);
        b += a.charAt(c >>> 4 & 15) + a.charAt(c & 15)
    }
    return b
}
function rstr2b64(d) {
    for (var a = "", b = d.length, c = 0; c < b; c += 3)
        for (var e = d.charCodeAt(c) << 16 | (c + 1 < b ? d.charCodeAt(c + 1) << 8 : 0) | (c + 2 < b ? d.charCodeAt(c + 2) : 0), f = 0; f < 4; f++)
            a += c * 8 + f * 6 > d.length * 8 ? b64pad : "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(e >>> 6 * (3 - f) & 63);
    return a
}
function rstr2any(d, a) {
    var b = a.length, c, e, f, g, h, i = Array(Math.ceil(d.length / 2));
    for (c = 0; c < i.length; c++)
        i[c] = d.charCodeAt(c * 2) << 8 | d.charCodeAt(c * 2 + 1);
    var j = Math.ceil(d.length * 8 / (Math.log(a.length) / Math.log(2)));
    d = Array(j);
    for (e = 0; e < j; e++) {
        h = Array();
        for (c = g = 0; c < i.length; c++) {
            g = (g << 16) + i[c];
            f = Math.floor(g / b);
            g -= f * b;
            if (h.length > 0 || f > 0)
                h[h.length] = f
        }
        d[e] = g;
        i = h
    }
    b = "";
    for (c = d.length - 1; c >= 0; c--)
        b += a.charAt(d[c]);
    return b
}
function str2rstr_utf8(d) {
    for (var a = "", b = -1, c, e; ++b < d.length; ) {
        c = d.charCodeAt(b);
        e = b + 1 < d.length ? d.charCodeAt(b + 1) : 0;
        if (55296 <= c && c <= 56319 && 56320 <= e && e <= 57343) {
            c = 65536 + ((c & 1023) << 10) + (e & 1023);
            b++
        }
        if (c <= 127)
            a += String.fromCharCode(c);
        else if (c <= 2047)
            a += String.fromCharCode(192 | c >>> 6 & 31, 128 | c & 63);
        else if (c <= 65535)
            a += String.fromCharCode(224 | c >>> 12 & 15, 128 | c >>> 6 & 63, 128 | c & 63);
        else if (c <= 2097151)
            a += String.fromCharCode(240 | c >>> 18 & 7, 128 | c >>> 12 & 63, 128 | c >>> 6 & 63, 128 | c & 63)
    }
    return a
}
function str2rstr_utf16le(d) {
    for (var a = "", b = 0; b < d.length; b++)
        a += String.fromCharCode(d.charCodeAt(b) & 255, d.charCodeAt(b) >>> 8 & 255);
    return a
}
function str2rstr_utf16be(d) {
    for (var a = "", b = 0; b < d.length; b++)
        a += String.fromCharCode(d.charCodeAt(b) >>> 8 & 255, d.charCodeAt(b) & 255);
    return a
}
function rstr2binl(d) {
    for (var a = Array(d.length >> 2), b = 0; b < a.length; b++)
        a[b] = 0;
    for (b = 0; b < d.length * 8; b += 8)
        a[b >> 5] |= (d.charCodeAt(b / 8) & 255) << b % 32;
    return a
}
function binl2rstr(d) {
    for (var a = "", b = 0; b < d.length * 32; b += 8)
        a += String.fromCharCode(d[b >> 5] >>> b % 32 & 255);
    return a
}
function binl_md5(d, a) {
    d[a >> 5] |= 128 << a % 32;
    d[(a + 64 >>> 9 << 4) + 14] = a;
    a = 1732584193;
    for (var b = -271733879, c = -1732584194, e = 271733878, f = 0; f < d.length; f += 16) {
        var g = a
          , h = b
          , i = c
          , j = e;
        a = md5_ff(a, b, c, e, d[f + 0], 7, -680876936);
        e = md5_ff(e, a, b, c, d[f + 1], 12, -389564586);
        c = md5_ff(c, e, a, b, d[f + 2], 17, 606105819);
        b = md5_ff(b, c, e, a, d[f + 3], 22, -1044525330);
        a = md5_ff(a, b, c, e, d[f + 4], 7, -176418897);
        e = md5_ff(e, a, b, c, d[f + 5], 12, 1200080426);
        c = md5_ff(c, e, a, b, d[f + 6], 17, -1473231341);
        b = md5_ff(b, c, e, a, d[f + 7], 22, -45705983);
        a = md5_ff(a, b, c, e, d[f + 8], 7, 1770035416);
        e = md5_ff(e, a, b, c, d[f + 9], 12, -1958414417);
        c = md5_ff(c, e, a, b, d[f + 10], 17, -42063);
        b = md5_ff(b, c, e, a, d[f + 11], 22, -1990404162);
        a = md5_ff(a, b, c, e, d[f + 12], 7, 1804603682);
        e = md5_ff(e, a, b, c, d[f + 13], 12, -40341101);
        c = md5_ff(c, e, a, b, d[f + 14], 17, -1502002290);
        b = md5_ff(b, c, e, a, d[f + 15], 22, 1236535329);
        a = md5_gg(a, b, c, e, d[f + 1], 5, -165796510);
        e = md5_gg(e, a, b, c, d[f + 6], 9, -1069501632);
        c = md5_gg(c, e, a, b, d[f + 11], 14, 643717713);
        b = md5_gg(b, c, e, a, d[f + 0], 20, -373897302);
        a = md5_gg(a, b, c, e, d[f + 5], 5, -701558691);
        e = md5_gg(e, a, b, c, d[f + 10], 9, 38016083);
        c = md5_gg(c, e, a, b, d[f + 15], 14, -660478335);
        b = md5_gg(b, c, e, a, d[f + 4], 20, -405537848);
        a = md5_gg(a, b, c, e, d[f + 9], 5, 568446438);
        e = md5_gg(e, a, b, c, d[f + 14], 9, -1019803690);
        c = md5_gg(c, e, a, b, d[f + 3], 14, -187363961);
        b = md5_gg(b, c, e, a, d[f + 8], 20, 1163531501);
        a = md5_gg(a, b, c, e, d[f + 13], 5, -1444681467);
        e = md5_gg(e, a, b, c, d[f + 2], 9, -51403784);
        c = md5_gg(c, e, a, b, d[f + 7], 14, 1735328473);
        b = md5_gg(b, c, e, a, d[f + 12], 20, -1926607734);
        a = md5_hh(a, b, c, e, d[f + 5], 4, -378558);
        e = md5_hh(e, a, b, c, d[f + 8], 11, -2022574463);
        c = md5_hh(c, e, a, b, d[f + 11], 16, 1839030562);
        b = md5_hh(b, c, e, a, d[f + 14], 23, -35309556);
        a = md5_hh(a, b, c, e, d[f + 1], 4, -1530992060);
        e = md5_hh(e, a, b, c, d[f + 4], 11, 1272893353);
        c = md5_hh(c, e, a, b, d[f + 7], 16, -155497632);
        b = md5_hh(b, c, e, a, d[f + 10], 23, -1094730640);
        a = md5_hh(a, b, c, e, d[f + 13], 4, 681279174);
        e = md5_hh(e, a, b, c, d[f + 0], 11, -358537222);
        c = md5_hh(c, e, a, b, d[f + 3], 16, -722521979);
        b = md5_hh(b, c, e, a, d[f + 6], 23, 76029189);
        a = md5_hh(a, b, c, e, d[f + 9], 4, -640364487);
        e = md5_hh(e, a, b, c, d[f + 12], 11, -421815835);
        c = md5_hh(c, e, a, b, d[f + 15], 16, 530742520);
        b = md5_hh(b, c, e, a, d[f + 2], 23, -995338651);
        a = md5_ii(a, b, c, e, d[f + 0], 6, -198630844);
        e = md5_ii(e, a, b, c, d[f + 7], 10, 1126891415);
        c = md5_ii(c, e, a, b, d[f + 14], 15, -1416354905);
        b = md5_ii(b, c, e, a, d[f + 5], 21, -57434055);
        a = md5_ii(a, b, c, e, d[f + 12], 6, 1700485571);
        e = md5_ii(e, a, b, c, d[f + 3], 10, -1894986606);
        c = md5_ii(c, e, a, b, d[f + 10], 15, -1051523);
        b = md5_ii(b, c, e, a, d[f + 1], 21, -2054922799);
        a = md5_ii(a, b, c, e, d[f + 8], 6, 1873313359);
        e = md5_ii(e, a, b, c, d[f + 15], 10, -30611744);
        c = md5_ii(c, e, a, b, d[f + 6], 15, -1560198380);
        b = md5_ii(b, c, e, a, d[f + 13], 21, 1309151649);
        a = md5_ii(a, b, c, e, d[f + 4], 6, -145523070);
        e = md5_ii(e, a, b, c, d[f + 11], 10, -1120210379);
        c = md5_ii(c, e, a, b, d[f + 2], 15, 718787259);
        b = md5_ii(b, c, e, a, d[f + 9], 21, -343485551);
        a = safe_add(a, g);
        b = safe_add(b, h);
        c = safe_add(c, i);
        e = safe_add(e, j)
    }
    return [a, b, c, e]
}
function md5_cmn(d, a, b, c, e, f) {
    return safe_add(bit_rol(safe_add(safe_add(a, d), safe_add(c, f)), e), b)
}
function md5_ff(d, a, b, c, e, f, g) {
    return md5_cmn(a & b | ~a & c, d, a, e, f, g)
}
function md5_gg(d, a, b, c, e, f, g) {
    return md5_cmn(a & c | b & ~c, d, a, e, f, g)
}
function md5_hh(d, a, b, c, e, f, g) {
    return md5_cmn(a ^ b ^ c, d, a, e, f, g)
}
function md5_ii(d, a, b, c, e, f, g) {
    return md5_cmn(b ^ (a | ~c), d, a, e, f, g)
}
function safe_add(d, a) {
    var b = (d & 65535) + (a & 65535);
    return (d >> 16) + (a >> 16) + (b >> 16) << 16 | b & 65535
}
function bit_rol(d, a) {
    return d << a | d >>> 32 - a
}
;