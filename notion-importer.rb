class NotionImporter < Formula
  desc "CLI tool for importing property data into Notion"
  homepage "https://github.com/erice1031/homebrew-notion-importer"
  url "https://github.com/user-attachments/files/17813996/notion-importer-1.0.0.tar.gz"
  sha256 "b6082bccaaf704764fc7f7a1be7d76ea73e1d998877da9d10a5b14427578f055"
  license "MIT"

  depends_on "python@3.9"

  def install
    bin.install "notion-importer.py" => "notion-importer"
  end

  test do
    system "#{bin}/notion-importer", "--help"
  end
end
