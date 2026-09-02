import { useState } from "react";
import { Link, useNavigate, useSearchParams } from "react-router-dom";
import {
  ArrowRight,
  BriefcaseBusiness,
  LockKeyhole,
} from "lucide-react";

const API_URL = "http://127.0.0.1:8000";

function ResetPassword() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  const token = searchParams.get("token");

  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const [error, setError] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setMessage("");

    if (!token) {
      setError(
        "Ссылка для восстановления пароля недействительна."
      );
      return;
    }

    if (password.length < 8) {
      setError(
        "Пароль должен содержать не менее 8 символов."
      );
      return;
    }

    if (password !== confirmPassword) {
      setError(
        "Пароли не совпадают."
      );
      return;
    }

    setLoading(true);

    try {
      const response = await fetch(
        `${API_URL}/auth/reset-password`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            token,
            new_password: password,
          }),
        }
      );

      let data = null;

      try {
        data = await response.json();
      } catch {
        data = null;
      }

      if (!response.ok) {
        throw new Error(
          data?.detail ||
            "Не удалось изменить пароль."
        );
      }

      setMessage(
        data?.message ||
          "Пароль успешно изменён."
      );

      setTimeout(() => {
        navigate("/login");
      }, 1500);
    } catch (err) {
      setError(
        err.message ||
          "Не удалось изменить пароль."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="auth-page">
      <div className="auth-container">
        <div className="auth-brand">
          <div className="auth-brand-icon">
            <BriefcaseBusiness size={24} />
          </div>

          <span>JobMatcher</span>
        </div>

        <div className="auth-card">
          <div className="auth-header">
            <h1>Новый пароль</h1>

            <p>
              Введите новый пароль для вашего аккаунта.
            </p>
          </div>

          {message && (
            <div className="auth-success">
              {message}
            </div>
          )}

          {error && (
            <div className="auth-error">
              {error}
            </div>
          )}

          <form
            onSubmit={handleSubmit}
            className="auth-form"
          >
            <div className="form-group">
              <label htmlFor="password">
                Новый пароль
              </label>

              <div className="input-wrapper">
                <LockKeyhole size={18} />

                <input
                  id="password"
                  type="password"
                  placeholder="Введите новый пароль"
                  value={password}
                  onChange={(event) =>
                    setPassword(event.target.value)
                  }
                  required
                  minLength={8}
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="confirm-password">
                Подтвердите пароль
              </label>

              <div className="input-wrapper">
                <LockKeyhole size={18} />

                <input
                  id="confirm-password"
                  type="password"
                  placeholder="Повторите новый пароль"
                  value={confirmPassword}
                  onChange={(event) =>
                    setConfirmPassword(event.target.value)
                  }
                  required
                  minLength={8}
                />
              </div>
            </div>

            <button
              type="submit"
              className="auth-submit-button"
              disabled={loading}
            >
              {loading
                ? "Изменение..."
                : "Изменить пароль"}

              {!loading && (
                <ArrowRight size={18} />
              )}
            </button>
          </form>

          <div className="auth-footer">
            <Link to="/login">
              Вернуться к входу
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
}

export default ResetPassword;