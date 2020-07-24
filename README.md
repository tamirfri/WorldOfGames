# How to run this project:
1. in terminal:
```shell
image=$( docker build https://github.com/tamirfri/WorldOfGames.git | tail --bytes 13 )
docker run -tip 5000:5000 $image
```
2. enter this url:
<http://localhost:5000/>
