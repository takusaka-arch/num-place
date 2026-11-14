# Structural changes so the English app can live next to the Japanese one on the same github.io origin
P = [
('<meta property="og:url" content="https://takusaka-arch.github.io/sudoku/">', '<meta property="og:url" content="https://takusaka-arch.github.io/num-place/">'),
('<meta property="og:image" content="https://takusaka-arch.github.io/sudoku/icons/icon-512.png">', '<meta property="og:image" content="https://takusaka-arch.github.io/num-place/icons/icon-512.png">'),
('const APP_URL = "https://takusaka-arch.github.io/sudoku/";', 'const APP_URL = "https://takusaka-arch.github.io/num-place/";'),
# only unregister / clear this app's own service worker and caches (the Japanese app shares the origin)
('try { for (const r of await sw.getRegistrations()) await r.unregister(); } catch (e) {}', 'try { for (const r of await sw.getRegistrations()) if (new URL(r.scope).pathname === new URL("./", location.href).pathname) await r.unregister(); } catch (e) {}'),
('try { for (const k of await caches.keys()) await caches.delete(k); } catch (e) {}', 'try { for (const k of await caches.keys()) if (k.startsWith("num-place-")) await caches.delete(k); } catch (e) {}'),
]
