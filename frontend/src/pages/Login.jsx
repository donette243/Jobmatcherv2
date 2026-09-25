import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  ArrowRight,
  BriefcaseBusiness,
  LockKeyhole,
  Mail,
} from "lucide-react";
import { login } from "../services/api";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setLoading(true);

    try {
      const data = await login(email, password);

      const token =
        data?.access_token ||
        data?.token;

      if (!token) {
        throw new Error(
          "Сервер не вернул токен"
        );
      }

      localStorage.setItem("token", token);

      navigate("/dashboard");
    } catch (err) {
      setError(
        err.message ||
          "Не удалось войти в систему"
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
            <h1>С возвращением!</h1>

            <p>
              Войдите в систему, чтобы просматривать вакансии
              и рекомендации
            </p>
          </div>

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
              <label htmlFor="email">
                Адрес электронной почты
              </label>

              <div className="input-wrapper">
                <Mail size={18} />

                <input
                  id="email"
                  type="email"
                  placeholder="you@example.com"
                  value={email}
                  onChange={(event) =>
                    setEmail(event.target.value)
                  }
                  required
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="password">
                Пароль
              </label>

              <div className="input-wrapper">
                <LockKeyhole size={18} />

                <input
                  id="password"
                  type="password"
                  placeholder="Введите пароль"
                  value={password}
                  onChange={(event) =>
                    setPassword(event.target.value)
                  }
                  required
                />
              </div>
            </div>

            <div className="forgot-password">
              <Link to="/forgot-password">
                Забыли пароль?
              </Link>
            </div>

            <button
              type="submit"
              className="auth-submit-button"
              disabled={loading}
            >
              {loading
                ? "Выполняется вход..."
                : "Войти"}

              {!loading && (
                <ArrowRight size={18} />
              )}
            </button>
          </form>

          <div className="auth-footer">
            <span>
              У вас ещё нет аккаунта?
            </span>

            <Link to="/register">
              Создать аккаунт
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
}

export default Login;