1. **Oturum kaydı ve dışa aktarma:** Bir tatbikat boyunca P/S matrisi, hızlar ve olay günlüğü dosyaya yazılsın; sonradan açılıp karşılaştırılsın. “Dünkü koşuda MekoFd’nin aboneliği neden boştu?” gibi sorular için çok işe yarar.
2. **Zaman yönetimi görünümü:** Federelerin mantıksal zamanları, regulating/constrained durumları ve aralarındaki fark (lookahead, LBTS) tek bir grafikte gösterilsin. Zaman yönetimli NavySim senaryolarında en sık sorulan soru “kim herkesi bekletiyor?” olur.
3. **Federasyon yönetimi:** MOM üzerinden save/restore başlatma, bir federeyi duraklatma veya resign ettirme. Güçlü ama riskli; onay ve yetki adımı gerekir.

**Araştırma tarafı**

- P/S matrisi ve ağ grafiği FOM yapısal metrikleri çalışmasıyla doğrudan bağlantılı. Statik FOM metriklerinin yanına, çalışan bir federasyonda gerçekten kullanılan sınıf oranı, eşleşmemiş yayın/abonelik sayısı ve federe başına bağlantı derecesi gibi çalışma zamanı ölçümleri eklenebilir. Bunu ayrı bir “metrics export” (CSV/JSON) olarak çıkarmak, bir tez veya makale için veri toplamayı kolaylaştırır.
- Aynı analiz kodu (`PubSubAnalysis`) bir SimGe projesine veya FDD’ye uygulanırsa, federasyon kurulmadan önce P/S tutarlılığı statik olarak denetlenebilir. Yani “tasarım anı uyarısı” ile “çalışma anı uyarısı” karşılaştırılabilir.

### FedMonFd

Federation Monitor Federate (FedMonFd) — see its [release notes](FedMonFd/ReleaseNotes.md).

- `SetExceptionLogging` implementation to monitor and log RTI exceptions.
- Management functions for the federation (save / restore / pause).
- Show the federate's IP address.
