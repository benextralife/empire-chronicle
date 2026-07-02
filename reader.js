
      window.onerror = function(msg, url, line) {
        var art = document.getElementById('article');
        if (art) art.innerHTML = '<div class="error">載入失敗：' + msg + '<br><small>line ' + line + '</small></div>';
        return true;
      };
    