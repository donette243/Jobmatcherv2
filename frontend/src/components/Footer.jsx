import { BriefcaseBusiness, Heart } from "lucide-react";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-brand">
          <div className="footer-logo">
            <div className="footer-logo-icon">
              <BriefcaseBusiness size={20} />
            </div>

            <span>JobMatcher</span>
          </div>

          <p>
            Находите вакансии, которые действительно соответствуют
            вашим навыкам и профессиональному профилю.
          </p>
        </div>

        <div className="footer-links">
          <span>JobMatcher</span>

          <span>
            Умный поиск работы
          </span>
        </div>

        <div className="footer-bottom">
          <span>
            © {new Date().getFullYear()} JobMatcher
          </span>

          <span className="footer-made">
            Создано с
            <Heart size={14} />
          </span>
        </div>
      </div>
    </footer>
  );
}

export default Footer;

