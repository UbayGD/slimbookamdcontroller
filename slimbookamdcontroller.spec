Name:           slimbookamdcontroller
Version:        0.3.9beta
Release:        1%{?dist}
Summary:        Slimbook AMD Controller

License:        GPL

%description
Slimbook AMD Controller works by setting your CPU TDP value

%install
# Create the necessary directories
mkdir -p %{buildroot}/usr/share/slimbookamdcontroller
mkdir -p %{buildroot}/usr/lib/systemd/system-sleep/
mkdir -p %{buildroot}/usr/share/applications
mkdir -p %{buildroot}/usr/share/icons/hicolor
mkdir -p %{buildroot}/usr/share/slimbookamdcontroller/src
mkdir -p %{buildroot}/etc/udev/rules.d
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/polkit-1/actions/

# Copy the files to the respective directories
cp -r src %{buildroot}/usr/share/slimbookamdcontroller
cp -r post-suspension/* %{buildroot}/usr/lib/systemd/system-sleep/
cp -r slimbookamdcontroller.desktop %{buildroot}/usr/share/applications/
cp -r slimbookamdcontroller.desktop %{buildroot}/usr/share/slimbookamdcontroller
cp -r src/images/icons/* %{buildroot}/usr/share/icons/hicolor/
cp -r udev-rules/* %{buildroot}/etc/udev/rules.d/
cp -r bin/* %{buildroot}/usr/bin/
cp -r policykit/* %{buildroot}/usr/share/polkit-1/actions/

cp debian/postinst %{buildroot}/
chmod +x %{buildroot}/postinst

cp debian/postrm %{buildroot}/
chmod +x %{buildroot}/postrm

%files
/usr/share/slimbookamdcontroller
/usr/lib/systemd/system-sleep/
/usr/share/applications
/usr/share/icons/hicolor
/etc/udev/rules.d
/usr/bin/
/usr/share/polkit-1/actions/
/postinst
/postrm

%post
if [ $1 == 1 ];then
    ./postinst
fi

%preun
if [ $1 == 0 ];then
    ./postrm
fi
