import { useEffect, useState } from "react";
import {
  BriefcaseBusiness,
  CalendarDays,
  GraduationCap,
  Languages,
  Mail,
  MapPin,
  Save,
  UserRound,
} from "lucide-react";
import { getProfile, updateProfile } from "../services/api";

function Profile() {
  const [profile, setProfile] = useState({
    first_name: "",
    last_name: "",
    email: "",
    birth_date: "",
    city: "",
    education: "",
    experience_years: "",
    skills: "",
    languages: "",
    desired_position: "",
    desired_location: "",
    remote: false,
    min_salary: "",
  });

  const [loading, setLoading] = useState(true);
  const [saving, setSaving] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    const loadProfile = async () => {
      try {
        const data = await getProfile();

        const name = data?.name || "";
        const nameParts = name.trim().split(/\s+/);

        setProfile({
          first_name:
            nameParts.length > 1
              ? nameParts.slice(1).join(" ")
              : nameParts[0] || "",

          last_name:
            nameParts.length > 1
              ? nameParts[0]
              : "",

          email: data?.email || "",
          birth_date: data?.birth_date || "",
          city: data?.city || "",
          education: data?.education || "",
          experience_years:
            data?.experience_years ?? "",

          skills: Array.isArray(data?.skills)
            ? data.skills.join(", ")
            : data?.skills || "",

          languages: Array.isArray(data?.languages)
            ? data.languages.join(", ")
            : data?.languages || "",

          desired_position:
            data?.preference?.desired_position || "",

          desired_location:
            data?.preference?.desired_location || "",

          remote:
            data?.preference?.remote || false,

          min_salary:
            data?.preference?.min_salary ?? "",
        });
      } catch (err) {
        setError(
          err.message ||
            "Не удалось загрузить профиль."
        );
      } finally {
        setLoading(false);
      }
    };

    loadProfile();
  }, []);

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;

    setProfile((current) => ({
      ...current,
      [name]: type === "checkbox" ? checked : value,
    }));

    setMessage("");
    setError("");
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    setSaving(true);
    setMessage("");
    setError("");

    try {
      await updateProfile({
        ...profile,

        experience_years:
          profile.experience_years === ""
            ? null
            : Number(profile.experience_years),

        min_salary:
          profile.min_salary === ""
            ? null
            : Number(profile.min_salary),

        skills: profile.skills
          .split(",")
          .map((skill) => skill.trim())
          .filter(Boolean),

        languages: profile.languages
          .split(",")
          .map((language) => language.trim())
          .filter(Boolean),
      });

      setMessage(
        "Ваш профиль успешно сохранён."
      );
    } catch (err) {
      setError(
        err.message ||
          "Не удалось сохранить профиль."
      );
    } finally {
      setSaving(false);
    }
  };

  if (loading) {
    return (
      <main className="profile-page">
        <div className="loading-state">
          Загрузка профиля...
        </div>
      </main>
    );
  }

  return (
    <main className="profile-page">
      <div className="page-container">
        <section className="page-header">
          <span className="page-eyebrow">
            <UserRound size={16} />
            Профессиональный профиль
          </span>

          <h1>Мой профиль</h1>

          <p>
            Заполните свой профиль, чтобы повысить точность
            рекомендаций JobMatcher.
          </p>
        </section>

        <section className="profile-card">
          <div className="profile-card-header">
            <div className="profile-avatar">
              <UserRound size={28} />
            </div>

            <div>
              <h2>Личная информация</h2>

              <p>
                Эти данные помогают лучше определить ваш
                профессиональный профиль.
              </p>
            </div>
          </div>

          {error && (
            <div className="auth-error">
              {error}
            </div>
          )}

          {message && (
            <div className="auth-success">
              {message}
            </div>
          )}

          <form
            onSubmit={handleSubmit}
            className="profile-form"
          >
            <div className="profile-form-grid">
              <div className="form-group">
                <label htmlFor="first_name">
                  Имя
                </label>

                <div className="input-wrapper">
                  <UserRound size={18} />

                  <input
                    id="first_name"
                    name="first_name"
                    type="text"
                    value={profile.first_name}
                    onChange={handleChange}
                    placeholder="Ваше имя"
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="last_name">
                  Фамилия
                </label>

                <div className="input-wrapper">
                  <UserRound size={18} />

                  <input
                    id="last_name"
                    name="last_name"
                    type="text"
                    value={profile.last_name}
                    onChange={handleChange}
                    placeholder="Ваша фамилия"
                  />
                </div>
              </div>
            </div>

            <div className="profile-form-grid">
              <div className="form-group">
                <label htmlFor="email">
                  Адрес электронной почты
                </label>

                <div className="input-wrapper">
                  <Mail size={18} />

                  <input
                    id="email"
                    name="email"
                    type="email"
                    value={profile.email}
                    onChange={handleChange}
                    placeholder="you@example.com"
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="birth_date">
                  Дата рождения
                </label>

                <div className="input-wrapper">
                  <CalendarDays size={18} />

                  <input
                    id="birth_date"
                    name="birth_date"
                    type="date"
                    value={profile.birth_date}
                    onChange={handleChange}
                  />
                </div>
              </div>
            </div>

            <div className="profile-form-grid">
              <div className="form-group">
                <label htmlFor="city">
                  Город проживания
                </label>

                <div className="input-wrapper">
                  <MapPin size={18} />

                  <input
                    id="city"
                    name="city"
                    type="text"
                    value={profile.city}
                    onChange={handleChange}
                    placeholder="Москва"
                  />
                </div>
              </div>

              <div className="form-group">
                <label htmlFor="education">
                  Уровень образования
                </label>

                <div className="input-wrapper">
                  <GraduationCap size={18} />

                  <input
                    id="education"
                    name="education"
                    type="text"
                    value={profile.education}
                    onChange={handleChange}
                    placeholder="Магистратура, аспирантура..."
                  />
                </div>
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="experience_years">
                Профессиональный опыт
              </label>

              <div className="input-wrapper">
                <BriefcaseBusiness size={18} />

                <input
                  id="experience_years"
                  name="experience_years"
                  type="number"
                  min="0"
                  step="0.5"
                  value={profile.experience_years}
                  onChange={handleChange}
                  placeholder="Количество лет"
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="skills">
                Навыки
              </label>

              <div className="textarea-wrapper">
                <BriefcaseBusiness size={18} />

                <textarea
                  id="skills"
                  name="skills"
                  value={profile.skills}
                  onChange={handleChange}
                  placeholder="Python, FastAPI, SQL, Docker..."
                  rows={5}
                />
              </div>

              <small>
                Разделяйте навыки запятыми.
              </small>
            </div>

            <div className="form-group">
              <label htmlFor="languages">
                Языки
              </label>

              <div className="textarea-wrapper">
                <Languages size={18} />

                <textarea
                  id="languages"
                  name="languages"
                  value={profile.languages}
                  onChange={handleChange}
                  placeholder="Французский, Английский, Русский..."
                  rows={3}
                />
              </div>

              <small>
                Разделяйте языки запятыми.
              </small>
            </div>

            <div className="profile-card-header">
              <div className="profile-avatar">
                <BriefcaseBusiness size={24} />
              </div>

              <div>
                <h2>Профессиональные предпочтения</h2>

                <p>
                  Эти данные помогают улучшить соответствие
                  вашего профиля вакансиям.
                </p>
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="desired_position">
                Желаемая должность
              </label>

              <div className="input-wrapper">
                <BriefcaseBusiness size={18} />

                <input
                  id="desired_position"
                  name="desired_position"
                  type="text"
                  value={profile.desired_position}
                  onChange={handleChange}
                  placeholder="Backend Developer"
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="desired_location">
                Желаемое местоположение
              </label>

              <div className="input-wrapper">
                <MapPin size={18} />

                <input
                  id="desired_location"
                  name="desired_location"
                  type="text"
                  value={profile.desired_location}
                  onChange={handleChange}
                  placeholder="Москва"
                />
              </div>
            </div>

            <div className="form-group">
              <label htmlFor="min_salary">
                Желаемая минимальная зарплата
              </label>

              <div className="input-wrapper">
                <span>₽</span>

                <input
                  id="min_salary"
                  name="min_salary"
                  type="number"
                  min="0"
                  value={profile.min_salary}
                  onChange={handleChange}
                  placeholder="100000"
                />
              </div>
            </div>

            <label className="profile-checkbox">
              <input
                type="checkbox"
                name="remote"
                checked={profile.remote}
                onChange={handleChange}
              />

              <span>
                Я заинтересована в удалённой работе
              </span>
            </label>

            <button
              type="submit"
              className="primary-button save-button"
              disabled={saving}
            >
              <Save size={18} />

              {saving
                ? "Сохранение..."
                : "Сохранить профиль"}
            </button>
          </form>
        </section>
      </div>
    </main>
  );
}

export default Profile;

