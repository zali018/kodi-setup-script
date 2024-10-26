import xbmc
import xbmcgui
import xbmcaddon

def kodi_notification(title, message, time=5000):
    xbmcgui.Dialog().notification(title, message, xbmcgui.NOTIFICATION_INFO, time)

    def add_source(name, url):
        profile_path = xbmc.translatePath('special://profile/')
            sources_xml_path = profile_path + 'userdata/sources.xml'

                try:
                        with open(sources_xml_path, 'r') as f:
                                    content = f.read()
                                        except FileNotFoundError:
                                                content = '<sources><files></files></sources>'

                                                    if name not in content:
                                                            content = content.replace('</files>', f'<source><name>{name}</name><path pathversion="1">{url}</path></source></files>')
                                                                    with open(sources_xml_path, 'w') as f:
                                                                                f.write(content)
                                                                                        kodi_notification(f"Source Added", f"Added {name} source.")

                                                                                        def install_from_zip(url, repo_name):
                                                                                            xbmc.executebuiltin(f"InstallFromZip({url})")
                                                                                                kodi_notification("Repository Installed", f"{repo_name} installed.")

                                                                                                def install_addon(addon_id):
                                                                                                    xbmc.executebuiltin(f"InstallAddon({addon_id})")
                                                                                                        kodi_notification("Addon Installed", f"{addon_id} installed.")

                                                                                                        def configure_kodi_settings():
                                                                                                            xbmc.executebuiltin("ActivateWindow(Settings)")
                                                                                                                xbmc.executebuiltin('SetSetting("subtitles.language", "forced_only")')  # Forced subtitles only
                                                                                                                    xbmc.executebuiltin('SetSetting("general.showparentdiritems", false)')  # Disable parent folder items
                                                                                                                        xbmc.executebuiltin('SetSetting("addons.unknownsources", true)')  # Enable unknown sources
                                                                                                                            kodi_notification("Settings Configured", "Basic Kodi settings configured.")

                                                                                                                            def install_fen_light():
                                                                                                                                add_source('fenlight', 'https://tikipeter.github.io/packages')
                                                                                                                                    install_from_zip('plugin.video.fenlight-x.x.x.zip', 'Fen Light')

                                                                                                                                    def install_cocoscrapers():
                                                                                                                                        add_source('cocoscrapers', 'https://cocojoe2411.github.io')
                                                                                                                                            install_from_zip('repository.cocoscrapers-x.x.x.zip', 'CocoScrapers')
                                                                                                                                                install_addon('script.module.cocoscrapers')

                                                                                                                                                def install_fentastic():
                                                                                                                                                    add_source('fentastic', 'https://ivarbrandt.github.io/repository.ivarbrandt')
                                                                                                                                                        install_from_zip('repository.ivarbrandti-x.x.x.zip', 'Fentastic')
                                                                                                                                                            install_addon('skin.fentastic')

                                                                                                                                                            def authorize_real_debrid():
                                                                                                                                                                real_debrid_code = xbmcgui.Dialog().input("Enter Real Debrid Authorization Code")
                                                                                                                                                                    xbmc.executebuiltin(f"RunPlugin(plugin://plugin.video.fenlight?debrid&code={real_debrid_code})")
                                                                                                                                                                        kodi_notification("Real Debrid Authorized", "Fen Light authorized with Real Debrid.")

                                                                                                                                                                        def authorize_trakt():
                                                                                                                                                                            trakt_code = xbmcgui.Dialog().input("Enter Trakt Authorization Code")
                                                                                                                                                                                xbmc.executebuiltin(f"RunPlugin(plugin://plugin.video.fenlight?trakt&code={trakt_code})")
                                                                                                                                                                                    kodi_notification("Trakt Authorized", "Fen Light authorized with Trakt.")

                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                        configure_kodi_settings()
                                                                                                                                                                                            install_fen_light()
                                                                                                                                                                                                install_cocoscrapers()
                                                                                                                                                                                                    install_fentastic()
                                                                                                                                                                                                        authorize_real_debrid()
                                                                                                                                                                                                            authorize_trakt()

                                                                                                                                                                                                                kodi_notification("Setup Complete", "Kodi setup with Fen Light, CocoScrapers, Fentastic completed.")