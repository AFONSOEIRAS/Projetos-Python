# Internet Speed tester
# pip install speedtest-cli
#pip uninstall speedtest-cli
import speedtest

# Crie uma instância do Speedtest
st = speedtest.Speedtest()
# Defina o melhor servidor
st.get_best_server()

# Teste a velocidade de download
download_speed = st.download() / 1_000_000  # Converta para Mbps
print(f"Velocidade de Download: {download_speed} Mbps")

# Teste a velocidade de upload
upload_speed = st.upload() / 1_000_000  # Converta para Mbps
print(f"Velocidade de Upload: {upload_speed} Mbps")

# Teste o Ping
ping = st.results.ping
print(f"Latência (Ping): {ping} ms")
