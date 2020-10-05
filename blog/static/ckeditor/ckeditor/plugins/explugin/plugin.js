( function() {
	'use strict';

	CKEDITOR.plugins.add( 'explugin', {
		requires: 'balloontoolbar,link,openlink',

		init: function( editor ) {
			editor.ui.addButton( 'OpenLink', {
				command: 'openLink',
				toolbar: 'links,50',
				label: editor.lang.openlink.menu
			} );

			editor.balloonToolbars.create( {
				buttons: 'OpenLink,Link,Unlink',
				cssSelector: 'a'
            } );
            editor.balloonToolbars.create( {
				buttons: 'Link,Unlink,Image',
				widgets: 'image'
            } );
            
          
       
        
		}
	} );
} )();