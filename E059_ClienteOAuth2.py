"""
Cliente OAuth2 con requests-oauthlib
Crea un cliente que autentique contra una API OAuth2:
text
- Obtener código de autorización (URL)
- Intercambiar código por token
- Usar token Bearer para llamadas API
- Refrescar token automáticamente
Maneja todos los códigos de error HTTP OAuth2.
"""

# Programa 59: Cliente OAuth2 completo
# pip install requests requests-oauthlib

from requests_oauthlib import OAuth2Session
import webbrowser
import urllib.parse


class ClienteOAuth2:
    """
    Cliente OAuth2 Authorization Code Flow completo.
    """
    
    def __init__(self, client_id, client_secret, redirect_uri="http://localhost:8080"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.token = None
        self.oauth = None
    
    def obtener_url_autorizacion(self, auth_url, scope):
        """
        Genera URL de autorización y la abre en navegador.
        """
        self.oauth = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri, scope=scope)
        url_autorizacion, state = self.oauth.authorization_url(auth_url)
        print(f"🔗 Abre esta URL en tu navegador:\n{url_autorizacion}")
        webbrowser.open(url_autorizacion)
        return state
    
    def obtener_token_autorizacion(self, token_url, state, codigo_autorizacion):
        """
        Intercambia código por token de acceso.
        """
        try:
            self.token = self.oauth.fetch_token(
                token_url,
                client_secret=self.client_secret,
                authorization_response=codigo_autorizacion,
                state=state
            )
            print("✅ Token obtenido correctamente")
            return True
        except Exception as e:
            print(f"❌ Error obteniendo token: {e}")
            return False
    
    def hacer_llamada_api(self, api_url):
        """
        Hace llamada protegida con token Bearer.
        """
        if not self.token:
            print("❌ No hay token válido")
            return None
        
        headers = {"Authorization": f"Bearer {self.token['access_token']}"}
        try:
            respuesta = self.oauth.get(api_url, headers=headers)
            respuesta.raise_for_status()
            return respuesta.json()
        except Exception as e:
            print(f"❌ Error API: {e}")
            return None
    
    def refrescar_token(self, token_refresh_url):
        """
        Refresca token automáticamente.
        """
        if not self.token or "refresh_token" not in self.token:
            print("❌ No hay refresh token")
            return False
        
        try:
            nuevos_datos = self.oauth.refresh_token(
                token_refresh_url,
                refresh_token=self.token["refresh_token"],
                client_id=self.client_id,
                client_secret=self.client_secret
            )
            self.token = nuevos_datos
            print("🔄 Token refrescado")
            return True
        except Exception as e:
            print(f"❌ Error refrescando: {e}")
            return False


def main():
    """
    Demo con GitHub OAuth2 (usa tus credenciales de https://github.com/settings/apps).
    """
    # Configuración GitHub OAuth App
    CLIENT_ID = "TU_CLIENT_ID"
    CLIENT_SECRET = "TU_CLIENT_SECRET"
    
    AUTH_URL = "https://github.com/login/oauth/authorize"
    TOKEN_URL = "https://github.com/login/oauth/access_token"
    API_URL = "https://api.github.com/user"
    REFRESH_URL = TOKEN_URL
    
    scope = ["user"]
    
    cliente = ClienteOAuth2(CLIENT_ID, CLIENT_SECRET)
    
    print("🔐 OAuth2 Authorization Code Flow")
    state = cliente.obtener_url_autorizacion(AUTH_URL, scope)
    
    # Simular callback (copiar URL del navegador)
    print("\n📋 Copia la URL completa del navegador y pégala aquí:")
    url_callback = input("URL de callback: ")
    
    # Extraer código de la URL
    codigo = urllib.parse.parse_qs(urllib.parse.urlparse(url_callback).query).get("code", [None])[0]
    if not codigo:
        print("❌ No se encontró código de autorización")
        return
    
    if cliente.obtener_token_autorizacion(TOKEN_URL, state, f"{cliente.redirect_uri}?code={codigo}"):
        # Llamada API
        datos_usuario = cliente.hacer_llamada_api(API_URL)
        if datos_usuario:
            print(f"\n👤 Usuario autenticado:")
            print(f"  Login: {datos_usuario.get('login')}")
            print(f"  Nombre: {datos_usuario.get('name')}")
        
        # Refresh token (simulado)
        cliente.refrescar_token(REFRESH_URL)


if __name__ == "__main__":
    main()
