class NotionImporter < Formula
  desc "CLI tool for importing property data into Notion"
  homepage "https://github.com/erice1031/homebrew-notion-importer"
  url "https://github.com/erice1031/homebrew-notion-importer/blob/main/notion-importer-1.0.0.tar.gz"
  sha256 "5830a901068e60e1feaa85d08d5964c6c542cf955b1952cc9c5e477fc0ca6bbd"
  license "MIT"

  depends_on "python@3.9"

  def install
    bin.install "notion-importer.py" => "notion-importer"
  end

  test do
    system "#{bin}/notion-importer", "--help"
  end
end
