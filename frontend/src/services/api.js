const API_URL = "http://127.0.0.1:8000";

async function request(endpoint, options = {}) {
  const token = localStorage.getItem("token");

  const headers = {
    ...(options.headers || {}),
  };

  if (token) {
    headers.Authorization = `Bearer ${token}`;
  }

  const response = await fetch(`${API_URL}${endpoint}`, {
    ...options,
    headers,
  });

  let data = null;

  try {
    data = await response.json();
  } catch {
    data = null;
  }

  if (!response.ok) {
    const detail =
      data?.detail ||
      data?.message ||
      "Произошла ошибка.";

    throw new Error(
      typeof detail === "string"
        ? detail
        : "Произошла ошибка."
    );
  }

  return data;
}

export async function login(email, password) {
  return request("/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });
}

export async function register(email, password) {
  return request("/auth/register", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
      password,
    }),
  });
}

export async function forgotPassword(email) {
  return request("/auth/forgot-password", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      email,
    }),
  });
}

export async function getJobs() {
  return request("/jobs");
}

export async function getProfile() {
  return request("/profile");
}

export async function updateProfile(profile) {
  return request("/profile", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(profile),
  });
}

export async function uploadCV(file) {
  const formData = new FormData();

  formData.append("file", file);

  return request("/cv/upload", {
    method: "POST",
    body: formData,
  });
}

export async function getRecommendations() {
  return request("/recommendations");
}

export function logout() {
  localStorage.removeItem("token");
}