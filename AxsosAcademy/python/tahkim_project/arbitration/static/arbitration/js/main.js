// تبديل طريقة الحجز: واتساب مباشر أو نموذج من داخل الموقع
document.addEventListener("DOMContentLoaded", function () {
  const mWhatsapp = document.getElementById("mWhatsapp");
  const mSite = document.getElementById("mSite");
  const whatsappArea = document.getElementById("whatsappArea");
  const siteArea = document.getElementById("siteArea");

  if (!mWhatsapp || !mSite) return;

  function selectMethod(method) {
    [mWhatsapp, mSite].forEach((el) => el.classList.remove("selected"));
    if (method === "whatsapp") {
      mWhatsapp.classList.add("selected");
      whatsappArea.style.display = "block";
      siteArea.style.display = "none";
    } else {
      mSite.classList.add("selected");
      siteArea.style.display = "block";
      whatsappArea.style.display = "none";
    }
  }

  mWhatsapp.addEventListener("click", () => selectMethod("whatsapp"));
  mSite.addEventListener("click", () => selectMethod("site"));
});

// نسخ رابط تأكيد الحجز إلى الحافظة
function copyConfirmLink(btn, url) {
  navigator.clipboard.writeText(url).then(() => {
    const original = btn.innerText;
    btn.innerText = "تم النسخ ✓";
    setTimeout(() => (btn.innerText = original), 1800);
  });
}

/* ============================================================
   الساعة والتاريخ بالتوقيت المحلي لجهاز الزائر (تتحدث كل ثانية)
   ============================================================ */
function updateClock() {
  const el = document.getElementById("liveClock");
  if (!el) return;
  const now = new Date();
  const locale = navigator.language || "ar";
  const formatted = new Intl.DateTimeFormat(locale, {
    weekday: "short",
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit",
  }).format(now);
  el.textContent = formatted;
}
setInterval(updateClock, 1000);
document.addEventListener("DOMContentLoaded", updateClock);

/* ============================================================
   الوضع الداكن (يُحفظ في المتصفح فيبقى محفوظاً بين الزيارات)
   ============================================================ */
function applyTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  const btn = document.getElementById("darkModeBtn");
  if (btn) btn.textContent = theme === "dark" ? "☀️" : "🌙";
}
function initTheme() {
  const saved = localStorage.getItem("site-theme") || "light";
  applyTheme(saved);
  const btn = document.getElementById("darkModeBtn");
  if (btn) {
    btn.addEventListener("click", () => {
      const current = document.documentElement.getAttribute("data-theme") || "light";
      const next = current === "dark" ? "light" : "dark";
      localStorage.setItem("site-theme", next);
      applyTheme(next);
    });
  }
}
document.addEventListener("DOMContentLoaded", initTheme);

/* ============================================================
   لوحة إتاحة القراءة: تكبير/تصغير الخط + تباين عالٍ
   ============================================================ */
function applyFontScale(scale) {
  document.documentElement.style.fontSize = scale + "%";
}
function increaseFont() {
  let scale = parseInt(localStorage.getItem("site-font-scale") || "100", 10);
  scale = Math.min(scale + 12, 148);
  localStorage.setItem("site-font-scale", scale);
  applyFontScale(scale);
}
function decreaseFont() {
  let scale = parseInt(localStorage.getItem("site-font-scale") || "100", 10);
  scale = Math.max(scale - 12, 76);
  localStorage.setItem("site-font-scale", scale);
  applyFontScale(scale);
}
function toggleContrast() {
  const isOn = document.documentElement.classList.toggle("high-contrast");
  localStorage.setItem("site-high-contrast", isOn ? "1" : "0");
}
function resetAccessibility() {
  localStorage.setItem("site-font-scale", "100");
  localStorage.setItem("site-high-contrast", "0");
  applyFontScale(100);
  document.documentElement.classList.remove("high-contrast");
}
function initAccessibility() {
  const scale = parseInt(localStorage.getItem("site-font-scale") || "100", 10);
  applyFontScale(scale);
  if (localStorage.getItem("site-high-contrast") === "1") {
    document.documentElement.classList.add("high-contrast");
  }
  const a11yBtn = document.getElementById("a11yBtn");
  const a11yPanel = document.getElementById("a11yPanel");
  if (a11yBtn && a11yPanel) {
    a11yBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      a11yPanel.classList.toggle("open");
    });
    document.addEventListener("click", (e) => {
      if (!a11yPanel.contains(e.target) && e.target !== a11yBtn) {
        a11yPanel.classList.remove("open");
      }
    });
  }
}
document.addEventListener("DOMContentLoaded", initAccessibility);

/* ============================================================
   دائرة التواصل العائمة: فتح/إغلاق لوحة التواصل
   ============================================================ */
document.addEventListener("DOMContentLoaded", function () {
  const fabBtn = document.getElementById("contactFabBtn");
  const panel = document.getElementById("contactPanel");
  if (!fabBtn || !panel) return;
  fabBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    panel.classList.toggle("open");
  });
  document.addEventListener("click", (e) => {
    if (!panel.contains(e.target) && e.target !== fabBtn) {
      panel.classList.remove("open");
    }
  });
});
