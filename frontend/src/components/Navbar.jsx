import { Link, useNavigate } from "react-router-dom";
import {
  BriefcaseBusiness,
  LogOut,
  Search,
  UserRound,
} from "lucide-react";

function Navbar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <header className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <div className="navbar-logo-icon">
            <BriefcaseBusiness size={21} />
          </div>

          <span>JobMatcher</span>
        </Link>

        <nav className="navbar-links">
          <Link to="/">
            Главная
          </Link>

          {token && (
            <>
              <Link to="/dashboard">
                Панель управления
              </Link>

              <Link to="/jobs">
                <Search size={16} />
                Вакансии
              </Link>

              <Link to="/recommendations">
                Рекомендации
              </Link>
            </>
          )}
        </nav>

        <div className="navbar-actions">
          {token ? (
            <>
              <Link
                to="/profile"
                className="navbar-profile"
                title="Мой профиль"
              >
                <UserRound size={19} />
              </Link>

              <button
                type="button"
                className="navbar-logout"
                onClick={handleLogout}
                title="Выйти"
              >
                <LogOut size={18} />
              </button>
            </>
          ) : (
            <>
              <Link
                to="/login"
                className="navbar-login"
              >
                Войти
              </Link>

              <Link
                to="/register"
                className="navbar-register"
              >
                Создать аккаунт
              </Link>
            </>
          )}
        </div>
      </div>
    </header>
  );
}

export default Navbar;

