import { useState } from "react";
import { Link } from "react-router-dom";
import {
  ArrowRight,
  BriefcaseBusiness,
  Mail,
} from "lucide-react";
import { forgotPassword } from "../services/api";

function ForgotPassword() {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setMessage("");
    setError("");
    setLoading(true);

    try {
      const data = await forgotPassword(email);

      setMessage(
        data?.message ||
          "Если аккаунт с таким адресом существует, ссылка для восстановления пароля будет отправлена."
      );
    } catch (err) {
      setError(
        err.message ||
          "Не удалось отправить ссылку для восстановления пароля."
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
            <h1>Восстановление пароля</h1>

            <p>
              Введите адрес электронной почты, указанный
              при регистрации. Мы отправим вам ссылку
              для восстановления пароля.
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

            <button
              type="submit"
              className="auth-submit-button"
              disabled={loading}
            >
              {loading
                ? "Отправка..."
                : "Отправить ссылку"}

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

export default ForgotPassword;