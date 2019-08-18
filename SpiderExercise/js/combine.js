var l = 0;
window.CharAnimate = function(e, c) {
    l && l.j();
    l = this;
    this.u = e;
    this.s = c;
    m("eStroke");
    this.f = new n;
    this.f.parse(this.u);
    var d = new p;
    d.parse(this.s);
    this.f.i("eStroke");
    this.f.o("eStroke", d);
    this.j = function() {
        this.f.j()
    }
}
;
function q(e, c) {
    function d(b) {
        m("eStroke");
        b.f = new n;
        b.f.parse(b.u[b.q]);
        var a = new p;
        a.parse(b.s[b.q]);
        b.f.i("eStroke");
        b.f.o("eStroke", a);
        b.b = setTimeout(function() {
            f(b)
        }, 10)
    }
    function f(b) {
        !b.f || !b.f.r() ? (++b.q,
        b.b = b.q >= b.s.length ? 0 : setTimeout(function() {
            animTimer = setTimeout(function() {
                d(b)
            }, 500)
        }, 500)) : b.b = setTimeout(function() {
            f(b)
        }, 10)
    }
    r && r.j();
    r = this;
    this.u = e;
    this.s = c;
    this.f = this.q = 0;
    clearTimeout(this.b);
    e.length && d(this);
    this.j = function() {
        clearTimeout(this.b);
        this.f && this.f.j()
    }
}
var r = 0;
window.startAnimate = function(e, c) {
    r = new q(e,c)
}
;
window.newContour = function(e, c) {
    0 != cvec && cvec.j();
    m("eStroke");
    cvec = new n;
    cvec.parse(e);
    var d = new p;
    d.parse(c);
    cvec.i("eStroke");
    cvec.o("eStroke", d)
}
;
function m(e) {
    e = document.getElementById(e);
    var c = e.getContext("2d");
    setLineDash(c, [10, 2, 2, 2]);
    c.fillStyle = bgcolor;
    c.fillRect(0, 0, e.width, e.width);
    c.beginPath();
    "Star" == plan ? (c.moveTo(0, 0),
    c.lineTo(e.width, e.width),
    c.moveTo(e.width, 0),
    c.lineTo(0, e.width),
    c.moveTo(e.width / 2, 0),
    c.lineTo(e.width / 2, e.width),
    c.moveTo(0, e.width / 2),
    c.lineTo(e.width, e.width / 2)) : "Four Square" == plan ? (c.moveTo(0, 0),
    c.moveTo(e.width / 2, 0),
    c.lineTo(e.width / 2, e.width),
    c.moveTo(0, e.width / 2),
    c.lineTo(e.width, e.width / 2)) : "Nine Square" == plan && (c.moveTo(0, 0),
    c.moveTo(e.width / 3, 0),
    c.lineTo(e.width / 3, e.width),
    c.moveTo(2 * e.width / 3, 0),
    c.lineTo(2 * e.width / 3, e.width),
    c.moveTo(0, e.width / 3),
    c.lineTo(e.width, e.width / 3),
    c.moveTo(0, 2 * e.width / 3),
    c.lineTo(e.width, 2 * e.width / 3));
    c.strokeStyle = planColor;
    c.stroke()
}
window.init = function(e) {
    m("eStroke");
    e && (e.action = "/common/fcg/estroke1.fcg?task=getPhrase",
    e.submit())
}
;
window.drawPlan = m;
window.finalize = function(e) {
    e.j()
}
;
window.isAnimating = function(e) {
    return e.r()
}
;
function u(e, c, d) {
    this.x = e;
    this.y = c;
    this.p = d
}
function v() {
    function e(b, a) {
        a.a > a.n ? a.b = 0 : (b.putImageData(a.m, a.c, a.d),
        a.a += eval(speed),
        b.save(),
        b.beginPath(),
        b.rect(a.g, a.d, a.a - a.g, a.l - a.d),
        b.clip(),
        b.beginPath(),
        a.i(b),
        b.fill(),
        b.restore(),
        a.b = setTimeout(function() {
            e(b, a)
        }, 20))
    }
    function c(b, a) {
        a.a > a.n ? a.b = 0 : (b.putImageData(a.m, a.c, a.d),
        a.a += eval(speed),
        b.save(),
        b.beginPath(),
        b.rect(a.c, a.g, a.k - a.c, a.a - a.g),
        b.clip(),
        b.beginPath(),
        a.i(b),
        b.fill(),
        b.restore(),
        a.b = setTimeout(function() {
            c(b, a)
        }, 20))
    }
    function d(b, a) {
        a.a < a.n ? a.b = 0 : (b.putImageData(a.m, a.c, a.d),
        a.a -= eval(speed),
        b.save(),
        b.beginPath(),
        b.rect(a.a, a.d, a.g - a.a, a.l - a.d),
        b.clip(),
        b.beginPath(),
        a.i(b),
        b.fill(),
        b.restore(),
        a.b = setTimeout(function() {
            d(b, a)
        }, 20))
    }
    function f(b, a) {
        a.a < a.n ? a.b = 0 : (b.putImageData(a.m, a.c, a.d),
        a.a -= eval(speed),
        b.save(),
        b.beginPath(),
        b.rect(a.c, a.a, a.k - a.c, a.g - a.a),
        b.clip(),
        b.beginPath(),
        a.i(b),
        b.fill(),
        b.restore(),
        a.b = setTimeout(function() {
            f(b, a)
        }, 20))
    }
    this.c = 1E4;
    this.k = 0;
    this.d = 1E4;
    this.m = this.G = this.l = 0;
    this.w = [];
    this.add = function(b) {
        this.c > b.x && (this.c = b.x);
        this.k < b.x && (this.k = b.x);
        this.d > b.y && (this.d = b.y);
        this.l < b.y && (this.l = b.y);
        this.w.push(b)
    }
    ;
    this.r = function() {
        return 0 != this.b
    }
    ;
    this.j = function() {
        clearTimeout(this.b)
    }
    ;
    this.D = function(b) {
        this.m && b.putImageData(this.m, this.c, this.d)
    }
    ;
    this.o = function(b, a) {
        this.m = b.getImageData(this.c, this.d, this.k - this.c, this.l - this.d);
        switch (a & 3) {
        case 0:
            this.g = this.c;
            this.n = this.k;
            this.a = this.g;
            e(b, this);
            break;
        case 1:
            this.g = this.d;
            this.n = this.l;
            this.a = this.g;
            c(b, this);
            break;
        case 2:
            this.g = this.k;
            this.n = this.c;
            this.a = this.g;
            d(b, this);
            break;
        case 3:
            this.g = this.l,
            this.n = this.d,
            this.a = this.g,
            f(b, this)
        }
    }
    ;
    this.i = function(b) {
        var a = this.w, c = !1, d;
        if (a[0].p)
            d = a[0];
        else if (a[1].p) {
            var e = (a[0].x + a[1].x) / 2
              , f = (a[0].y + a[1].y) / 2;
            d = new u(e,f,1)
        } else
            d = a[0];
        for (var e = d.x, f = d.y, j = a.length, h = 1; h <= j; ++h) {
            var s = a[h % j].x
              , t = a[h % j].y;
            if (a[h % j].p) {
                if (1 < h || 1 == h && a[0].p)
                    c ? b.lineTo(e, f) : (b.moveTo(e, f),
                    c = !0),
                    b.lineTo(s, t);
                e = s;
                f = t;
                d = a[h % j]
            } else
                a[(h + 1) % j].p ? (d = this.v(b, d, a[h % j], a[(h + 1) % j], c),
                c = !0,
                e = d.x,
                f = d.y,
                ++h) : (f = a[(h + 1) % j],
                e = (a[h % j].x + f.x) / 2,
                f = (a[h % j].y + f.y) / 2,
                d = this.v(b, d, a[h % j], new u(e,f,1), c),
                c = !0,
                e = d.x,
                f = d.y)
        }
    }
    ;
    this.v = function(b, a, c, d, e) {
        var f = a.x;
        a = a.y;
        e ? b.lineTo(f, a) : b.moveTo(f, a);
        b.quadraticCurveTo(c.x, c.y, d.x, d.y);
        return d
    }
}
function n() {
    function e(c, d, f) {
        if (-1 == d.a || !d.h[d.a].r()) {
            if (0 <= d.a && !(d.a < f.e.length && f.e[d.a + 1] & 128) && transientColor.length && !d.t) {
                d.b = setTimeout(function() {
                    d.t = !0;
                    var a = f.F(f.A(d.a));
                    if (0 <= a) {
                        for (var b = a; b <= d.a; ++b)
                            d.h[b].D(c);
                        for (b = a; b <= d.a; ++b)
                            c.save(),
                            c.beginPath(),
                            d.h[b].i(c),
                            a = strokeColor,
                            f.z(b) && (a = radicalColor),
                            c.fillStyle = a,
                            c.fill(),
                            c.restore()
                    }
                    e(c, d, f)
                }, 200);
                return
            }
            if (++d.a < f.e.length) {
                d.t = !1;
                var b = transientColor;
                b.length || (b = strokeColor,
                f.z(d.a) && (b = radicalColor));
                c.fillStyle = b;
                b = f.e[d.a];
                if (b & 128)
                    d.h[d.a].o(c, b);
                else {
                    d.b = setTimeout(function() {
                        d.h[d.a].o(c, f.e[d.a]);
                        d.b = setTimeout(function() {
                            e(c, d, f)
                        }, 10)
                    }, 500);
                    return
                }
            } else {
                d.b = 0;
                return
            }
        }
        d.b = setTimeout(function() {
            e(c, d, f)
        }, 10)
    }
    this.h = [];
    this.add = function(c) {
        this.h.push(c)
    }
    ;
    this.B = function(c) {
        for (var d = c.length, e = Math.floor(d / 3), b = "", a = 0; a < c.length; ++a) {
            var g = a - e;
            0 > g && (g += d);
            b = b.concat(String.fromCharCode(c.charCodeAt(g) ^ "Copyright EON Media Limited 1999-2006 - http://www.eon.com.hk, Unit C, 13/F Skyview Cliff, 49 Conduit Road MidLevels Hong Kong. All Rights Reserved".charCodeAt(g % 147) & 15))
        }
        return b
    }
    ;
    this.parse = function(c) {
        this.c = 1E4;
        this.k = 0;
        this.d = 1E4;
        this.l = 0;
        this.a = -1;
        this.b = 0;
        this.t = !1;
        c = this.B(c);
        for (var d = 2; d < c.length; ) {
            for (var e = new v, b = parseInt(c.substr(d, 3), 10), d = d + 3, a = 0; a < b; ++a) {
                var g = parseInt(c.substr(d, 4), 16)
                  , g = g ^ 62953;
                32267 < g && (g -= 65536);
                this.c > g && (this.c = g);
                this.k < g && (this.k = g);
                var d = d + 4
                  , k = parseInt(c.substr(d, 4), 16)
                  , k = k ^ 10935;
                32267 < k && (k -= 65536);
                this.d > k && (this.d = k);
                this.l < k && (this.l = k);
                d += 4;
                e.add(new u(g,k,"1" == c.charAt(d)));
                ++d
            }
            this.add(e)
        }
    }
    ;
    this.i = function(c) {
        c = document.getElementById(c).getContext("2d");
        c.beginPath();
        for (var d = 0; d < this.h.length; ++d)
            this.h[d].i(c);
        c.fillStyle = "#cccccc";
        c.fill()
    }
    ;
    this.o = function(c, d) {
        var f = document.getElementById(c).getContext("2d");
        this.a = -1;
        d.e.length && e(f, this, d)
    }
    ;
    this.r = function() {
        return 0 != this.b
    }
    ;
    this.j = function() {
        clearTimeout(this.b);
        for (var c = 0; c < this.h.length; ++c)
            this.h[c].j()
    }
}
;function p() {
    this.e = [];
    this.parse = function(e) {
        for (var c = 0; c < e.length; c += 2)
            this.e.push(parseInt(e.substr(c, 2), 16) & 255)
    }
    ;
    this.F = function(e) {
        for (var c = 0; c < this.e.length; ++c)
            if (!(this.e[c] & 128)) {
                if (0 == e)
                    return c;
                --e
            }
        return -1
    }
    ;
    this.C = function(e) {
        for (var c = !1, d = 0; d < this.e.length; ++d)
            if (!(this.e[d] & 128)) {
                c = this.e[d] & 64;
                if (0 == e)
                    break;
                --e
            }
        return c
    }
    ;
    this.z = function(e) {
        return this.e[e] & 64 ? !0 : this.C(this.A(e))
    }
    ;
    this.A = function(e) {
        for (var c = -1, d = 0; d <= e; ++d)
            this.e[d] & 128 || ++c;
        return c
    }
}
;