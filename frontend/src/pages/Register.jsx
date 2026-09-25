import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import {
  ArrowRight,
  BriefcaseBusiness,
  LockKeyhole,
  Mail,
} from "lucide-react";
import { register } from "../services/api";

function Register() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setError("");
    setSuccess("");
    setLoading(true);

    try {
      await register(email, password);

      setSuccess(
        "Ваш аккаунт успешно создан"
      );

      setTimeout(() => {
        navigate("/login");
      }, 1000);
    } catch (err) {
      setError(
        err.message ||
          "Не удалось создать аккаунт"
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
            <h1>Создайте аккаунт</h1>

            <p>
              Присоединяйтесь к JobMatcher и начинайте находить
              вакансии, которые соответствуют вашему профилю
            </p>
          </div>

          {error && (
            <div className="auth-error">
              {error}
            </div>
          )}

          {success && (
            <div className="auth-success">
              {success}
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
                  placeholder="Придумайте пароль"
                  value={password}
                  onChange={(event) =>
                    setPassword(event.target.value)
                  }
                  minLength={8}
                  required
                />
              </div>

              <small>
                Пароль должен содержать не менее 8 символов
              </small>
            </div>

            <button
              type="submit"
              className="auth-submit-button"
              disabled={loading}
            >
              {loading
                ? "Создание аккаунта..."
                : "Создать аккаунт"}

              {!loading && (
                <ArrowRight size={18} />
              )}
            </button>
          </form>

          <div className="auth-footer">
            <span>
              У вас уже есть аккаунт?
            </span>

            <Link to="/login">
              Войти
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
}

export default Register;

