class NotionImporter < Formula
  desc "CLI tool for importing property data into Notion"
  homepage "https://github.com/erice1031/homebrew-notion-importer"
  url "https://github.com/erice1031/homebrew-notion-importer/blob/main/notion-importer-1.0.0.tar.gz"
  sha256 "8ba659f9ac778999a2a7f263e9ee5e3fa7fd83a2dbe9cba62832c1c0cb44ce5e"
  license "MIT"

  depends_on "python@3.9"

  def install
    bin.install "notion-importer.py" => "notion-importer"
  end

  test do
    system "#{bin}/notion-importer", "--help"
  end
end
