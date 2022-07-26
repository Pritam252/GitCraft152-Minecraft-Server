# MIT License, Gitcraft Mod installer
# Place in the mods folder and run
# python mod_updater.py

import os
import requests


def download(url: str):
    dest_folder='./mods'
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)  # create folder if it does not exist

    filename = url.split('/')[-1].replace(" ", "_")  # be careful with file names
    file_path = os.path.join(dest_folder, filename)

    r = requests.get(url, stream=True)
    if r.ok:
        print("[MAIN/MOD_DOWNLOADER]: ", os.path.abspath(file_path), ' from ', url)
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 8):
                if chunk:
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())
    else:  # HTTP status code 4XX/5XX
        print("Download failed: status code {}\n{}".format(r.status_code, r.text))

download('https://media.forgecdn.net/files/3672/914/AsmodeusCore-1.12.2-0.0.30.jar')
# download('https://micdoodle8.com/new-builds/GC-1.12/280/Galacticraft-Planets-1.12.2-4.0.2.280.jar')
download('https://media.forgecdn.net/files/3676/89/GalaxySpace-1.12.2-2.0.18.jar')
download('https://media.forgecdn.net/files/2623/90/RedstoneFlux-1.12-2.1.0.6-universal.jar')
download('https://media.forgecdn.net/files/2567/263/CoFHWorld-1.12.2-1.2.0.5-universal.jar')
# download('https://micdoodle8.com/new-builds/GC-1.12/280/GalacticraftCore-1.12.2-4.0.2.280.jar')
download('https://media.forgecdn.net/files/3643/158/NuclearCraft-2.18zz-1.12.2.jar')
download('https://media.forgecdn.net/files/2785/465/Forgelin-1.8.4.jar')
download('https://media.forgecdn.net/files/2817/545/exnihilocreatio-1.12.2-0.4.7.2.jar')
download('https://media.forgecdn.net/files/3328/811/EnderIO-1.12.2-5.3.70.jar')
download('https://media.forgecdn.net/files/2972/849/EnderCore-1.12.2-0.5.76.jar')
download('https://media.forgecdn.net/files/2940/914/refinedstorage-1.6.16.jar')
download('https://media.forgecdn.net/files/3762/171/Immersive+Vehicles-1.12.2-21.2.0.jar')
download('https://media.forgecdn.net/files/3592/807/MTS_Official_Pack_V23.jar')
download('https://media.forgecdn.net/files/2915/363/CTM-MC1.12.2-1.0.2.31.jar')
download('https://media.forgecdn.net/files/2915/375/Chisel-MC1.12.2-1.0.2.45.jar')
download('https://media.forgecdn.net/files/2678/374/extrautils2-1.12-1.9.9.jar')
download('https://media.forgecdn.net/files/2817/545/exnihilocreatio-1.12.2-0.4.7.2.jar')
download('https://media.forgecdn.net/files/2966/941/ExCompressum_1.12.2-3.0.32.jar')
download('https://media.forgecdn.net/files/2618/890/tinyprogressions-1.12.2-3.3.31-Release.jar')
download('https://media.forgecdn.net/files/2713/386/Mantle-1.12-1.3.3.55.jar')
download('https://media.forgecdn.net/files/2902/483/TConstruct-1.12.2-2.13.0.183.jar')
download('https://media.forgecdn.net/files/2779/848/CodeChickenLib-1.12.2-3.2.3.358-universal.jar')
download('https://media.forgecdn.net/files/2735/197/MrTJPCore-1.12.2-2.1.4.43-universal.jar')
download('https://media.forgecdn.net/files/2755/790/ForgeMultipart-1.12.2-2.6.2.83-universal.jar')
download('https://media.forgecdn.net/files/2745/545/ProjectRed-1.12.2-4.9.4.120-Base.jar')
download('https://media.forgecdn.net/files/2745/548/ProjectRed-1.12.2-4.9.4.120-integration.jar')
download('https://media.forgecdn.net/files/2745/547/ProjectRed-1.12.2-4.9.4.120-fabrication.jar')
download('https://media.forgecdn.net/files/2904/825/Pam%27s+HarvestCraft+1.12.2zg.jar')
download('https://media.forgecdn.net/files/2974/106/ImmersiveEngineering-0.12-98.jar')
download('https://media.forgecdn.net/files/3382/321/immersivepetroleum-1.12.2-1.1.10.jar')
download('https://media.forgecdn.net/files/3437/738/ImmersiveRailroading-1.12.2-forge-1.9.1.jar')
download('https://media.forgecdn.net/files/3043/174/jei_1.12.2-4.16.1.302.jar')
# download('https://micdoodle8.com/new-builds/GC-1.12/280/MicdoodleCore-1.12.2-4.0.2.280.jar')
download('https://media.forgecdn.net/files/2825/260/TrackAPI-1.2.jar')
download('https://media.forgecdn.net/files/3654/955/UniversalModCore-1.12.2-forge-1.1.4-2b81e7.jar')
print('Done!')
