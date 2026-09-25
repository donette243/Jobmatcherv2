import { useState } from "react";
import {
  CheckCircle2,
  FileText,
  LoaderCircle,
  Upload,
} from "lucide-react";
import { uploadCV } from "../services/api";

function CV() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState("");
  const [error, setError] = useState("");

  const handleFileChange = (event) => {
    const selectedFile = event.target.files?.[0];

    setMessage("");
    setError("");

    if (!selectedFile) {
      return;
    }

    const allowedTypes = [
      "application/pdf",
      "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ];

    if (!allowedTypes.includes(selectedFile.type)) {
      setError("Выберите файл в формате PDF или DOCX");
      return;
    }

    setFile(selectedFile);
  };

  const handleUpload = async () => {
    if (!file) {
      setError("Выберите своё резюме");
      return;
    }

    setLoading(true);
    setMessage("");
    setError("");

    try {
      await uploadCV(file);

      setMessage("Ваше резюме успешно загружено");
    } catch (err) {
      setError(
        err.message || "Не удалось загрузить резюме"
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="cv-page">
      <div className="page-container">
        <section className="page-header">
          <div>
            <span className="page-eyebrow">
              <FileText size={16} />
              Моё резюме
            </span>

            <h1>Анализ резюме</h1>

            <p>
              Загрузите резюме, чтобы JobMatcher мог определить
              ваши навыки и сформировать профессиональный профиль
            </p>
          </div>
        </section>

        <section className="cv-upload-card">
          <div className="upload-icon">
            <Upload size={30} />
          </div>

          <h2>
            Загрузите резюме
          </h2>

          <p>
            Поддерживаемые форматы: PDF или DOCX
          </p>

          <label htmlFor="cv-file" className="upload-area">
            <FileText size={38} />

            <strong>
              {file
                ? file.name
                : "Нажмите, чтобы выбрать резюме"}
            </strong>

            <span>
              Рекомендуемый максимальный размер: 10 МБ
            </span>

            <input
              id="cv-file"
              type="file"
              accept=".pdf,.docx"
              onChange={handleFileChange}
            />
          </label>

          {file && (
            <div className="selected-file">
              <CheckCircle2 size={18} />

              <span>
                {file.name}
              </span>
            </div>
          )}

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

          <button
            type="button"
            className="primary-button upload-button"
            onClick={handleUpload}
            disabled={loading || !file}
          >
            {loading ? (
              <>
                <LoaderCircle
                  className="loading-spinner"
                  size={18}
                />
                Выполняется анализ...
              </>
            ) : (
              <>
                <Upload size={18} />
                Загрузить резюме
              </>
            )}
          </button>
        </section>
      </div>
    </main>
  );
}

export default CV;

