# vplusErp snippets

vplus FrameWork f/w 에 사용되는 스니펫 모음입니다.

intellisense에서 사용할 스니펫을 선택하고 `tab`키를 눌러 스니펫에 지정된 값으로 이동, 입력할 수 있습니다.

## Demo
![htmldemo](images/htmldemo.gif)





## javascript
|Prefix|Description|
|------|-----------|
|`v-grd-create`|기본 시트를 생성합니다.|
|`v-grd-e-bfRowChg`|행 이동 전 변경된 내용이 있으면 알림창을 띄우는 이벤트를 추가합니다.|
|`v-grd-e-RowChg`|행 이동 후 이전 행의 변경된 내용을 조회 값으로 되돌리는 이벤트를 추가합니다.|
|`v-grd-e-btnClk`|지정한 컬럼에 팝업 클릭 코드파인더를 생성하는 이벤트를 추가합니다.|
|`v-grd-e-keyUp`|[onButtonClick-onKeyUp] 바인딩하는 이벤트를 추가합니다.|
|`v-grd-fn-postCode`|그리드 버튼에 주소 API를 바인딩합니다.|
|`v-grd-fn-upload`|그리드에 첨부파일 팝업을 바인딩합니다.|
|`v-frm-fn-postCode`|폼 input에 주소 API를 바인딩합니다.|
|`v-frm-fn-upload`|폼에 첨부파일 팝업을 바인딩합니다.|
|`v-ajax-get-grd`|그리드 조회 공통함수를 추가합니다.|
|`v-ajax-set-grd`|그리드 저장 공통함수를 추가합니다.|
|`v-ajax-getSet-grd`|그리드 조회/저장 공통함수를 추가합니다.|
|`v-ajax-get-frm`|폼 조회 공통함수를 추가합니다.|
|`v-ajax-set-frm`|폼 저장 공통함수를 추가합니다.|
|`v-util-schChk`|조회 전 변경, 필수 항목을 체크합니다.|


## html
|Prefix|Description|
|------|-----------|
|`v-ui-vpbox`|기본 vpbox를 생성합니다.|
|`v-ui-vpbox-calAutoRow`|고정 높이를 가지는 상/하 div를 생성합니다.|
|`v-ui-form`|JSTL을 포함하는 기본 form을 생성합니다.|
|`v-ui-postcode`|우편번호 input 레이아웃을 생성합니다.|
|`v-ui-dialog`|다이얼로그 레이아웃을 생성합니다.|
|`v-tag-input`|input jstl을 생성합니다.|
|`v-tag-inputsimple`|필수 속성만을 가지는 input jstl을 생성합니다|
|`v-tag-radio`|radio jstl을 생성합니다.|
|`v-tag-radioComCd`|공통코드 radio jstl을 생성합니다.|
|`v-tag-checkbox`|checkbox jstl을 생성합니다.|
|`v-tag-chkboxComCd`|공통코드 checkbox jstl을 생성합니다.|
|`v-tag-select`|selectbox jstl을 생성합니다.|
|`v-tag-selectComCd`|공통코드 selectbox jstl을 생성합니다.|
|`v-tag-date`|date jstl을 생성합니다.|
|`v-tag-rangeDate`|range date jstl을 생성합니다.|
|`v-tag-codefind`|코드파인드 jstl을 생성합니다.|


## java
|Prefix|Description|
|------|-----------|
|`v-contoller-view`|화면이동|
|`v-contoller-get-Grd`|조회 - 그리드 타입|
|`v-contoller-get-Frm`|조회 - 폼 타입|
|`v-contoller-set-Grd`|조회 - 그리드 타입|
|`v-contoller-set-Frm`|조회 - 폼 타입|
|`v-service-get-list`|조회 - 리스트 타입|
|`v-service-get-map`|조회 - 맵 타입|
|`v-service-set-list`|저장 - 리스트 타입|
|`v-service-set-list-map`|저장 - 리스트 타입|
|`v-service-set-map`|저장 - 맵 타입|
|`v-serviceImpl-get-list`|조회 - 리스트 타입|
|`v-serviceImpl-get-map`|조회 - 리스트 타입|
|`v-serviceImpl-set-list`|조회 - 리스트 타입|
|`v-repository-get-void`|조회 - list|
|`v-repository-get-list`|조회 - list|
|`v-repository-set-map`|저장 - map|
|`v-repository-set-list`|저장 - map|


## xml
|Prefix|Description|
|------|-----------|
|`v-sessin-info`|조회 - 그리드|
|`v-get-procedure`|조회 - 그리드|
|`v-get-query`|조회 - 그리드|
|`v-set-procedure`|그리드조회|
|`v-set-query`|그리드조회|
