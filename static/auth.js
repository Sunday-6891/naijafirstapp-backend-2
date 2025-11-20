const API = "http://127.0.0.1:8000/api";
const $ = (id) => document.getElementById(id);

// Switch forms
$("show-login").onclick = () => {
  $("signup-box").style.display = "none";
  $("login-box").style.display = "block";
};
$("show-signup").onclick = () => {
  $("signup-box").style.display = "block";
  $("login-box").style.display = "none";
};

// Signup
$("signup-form").onsubmit = async (e) => {
  e.preventDefault();
  const data = {
    username: $("su-username").value,
    email: $("su-email").value,
    password: $("su-pass").value,
    password2: $("su-pass2").value,
  };
  const res = await fetch(`${API}/register/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  });
  const json = await res.json();
  if (res.ok) saveTokens(json);
  else alert(json.username || json.password || "Signup failed");
};

// Login
$("login-form").onsubmit = async (e) => {
  e.preventDefault();
  const res = await fetch(`${API}/login/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      username: $("li-username").value,
      password: $("li-pass").value,
    }),
  });
  const json = await res.json();
  if (res.ok) saveTokens(json);
  else alert("Wrong credentials");
};

// Save tokens + show success
function saveTokens({ user, access, refresh }) {
  localStorage.setItem("access", access);
  localStorage.setItem("refresh", refresh);
  localStorage.setItem("username", user.username);
  $("signup-box").style.display = "none";
  $("login-box").style.display = "none";
  $("success-box").style.display = "block";
  $("greeting-user").textContent = user.username;
}

// Call protected API
$("call-secret").onclick = async () => {
  const token = localStorage.getItem("access");
  const res = await fetch(`${API}/secret/`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (res.ok) {
    const json = await res.json();
    $("api-response").textContent = JSON.stringify(json, null, 2);
  } else if (res.status === 401) {
    await refreshToken();
    $("call-secret").click(); // retry
  }
};

// Refresh token when expired
async function refreshToken() {
  const res = await fetch(`${API}/refresh/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh: localStorage.getItem("refresh") }),
  });
  const json = await res.json();
  localStorage.setItem("access", json.access);
}

// Logout
$("logout").onclick = () => {
  localStorage.clear();
  location.reload();
};

// Auto-login if token exists
if (localStorage.getItem("access")) {
  $("greeting-user").textContent = localStorage.getItem("username");
  $("success-box").style.display = "block";
}